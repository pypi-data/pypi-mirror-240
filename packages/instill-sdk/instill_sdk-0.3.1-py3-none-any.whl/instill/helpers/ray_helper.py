import argparse
import struct
from enum import Enum

import numpy as np


class DataType(Enum):
    TYPE_BOOL = 1
    TYPE_UINT8 = 2
    TYPE_UINT16 = 3
    TYPE_UINT32 = 4
    TYPE_UINT64 = 5
    TYPE_INT8 = 6
    TYPE_INT16 = 7
    TYPE_INT32 = 8
    TYPE_INT64 = 9
    TYPE_FP16 = 10
    TYPE_FP32 = 11
    TYPE_FP64 = 12
    TYPE_STRING = 13


def serialize_byte_tensor(input_tensor):
    """
    Serializes a bytes tensor into a flat numpy array of length prepended
    bytes. The numpy array should use dtype of np.object_. For np.bytes_,
    numpy will remove trailing zeros at the end of byte sequence and because
    of this it should be avoided.
    Parameters
    ----------
    input_tensor : np.array
        The bytes tensor to serialize.
    Returns
    -------
    serialized_bytes_tensor : np.array
        The 1-D numpy array of type uint8 containing the serialized bytes in 'C' order.
    Raises
    ------
    InferenceServerException
        If unable to serialize the given tensor.
    """

    if input_tensor.size == 0:
        return ()

    # If the input is a tensor of string/bytes objects, then must flatten those
    # into a 1-dimensional array containing the 4-byte byte size followed by the
    # actual element bytes. All elements are concatenated together in "C" order.
    if (input_tensor.dtype == np.object_) or (input_tensor.dtype.type == np.bytes_):
        flattened_ls: list = []
        for obj in np.nditer(input_tensor, flags=["refs_ok"], order="C"):
            # If directly passing bytes to BYTES type,
            # don't convert it to str as Python will encode the
            # bytes which may distort the meaning
            assert isinstance(obj, np.ndarray)
            if input_tensor.dtype == np.object_:
                if isinstance(obj.item(), bytes):
                    s = obj.item()
                else:
                    s = str(obj.item()).encode("utf-8")
            else:
                s = obj.item()
            flattened_ls.append(struct.pack("<I", len(s)))
            flattened_ls.append(s)
        flattened = b"".join(flattened_ls)
        return flattened
    return None


def deserialize_bytes_tensor(encoded_tensor):
    """
    Deserializes an encoded bytes tensor into an
    numpy array of dtype of python objects

    Parameters
    ----------
    encoded_tensor : bytes
        The encoded bytes tensor where each element
        has its length in first 4 bytes followed by
        the content
    Returns
    -------
    string_tensor : np.array
        The 1-D numpy array of type object containing the
        deserialized bytes in 'C' order.

    """
    strs = []
    offset = 0
    val_buf = encoded_tensor
    while offset < len(val_buf):
        l = struct.unpack_from("<I", val_buf, offset)[0]
        offset += 4
        sb = struct.unpack_from("<{}s".format(l), val_buf, offset)[0]
        offset += l
        strs.append(sb)
    return np.array(strs, dtype=bytes)


class InstillRayModelConfig:
    def __init__(
        self,
        ray_actor_options: dict,
        ray_autoscaling_options: dict,
        max_concurrent_queries: int,
        og_model_path: str,
    ) -> None:
        og_model_string_parts = og_model_path.split("/")

        self.ray_actor_options = ray_actor_options
        self.ray_autoscaling_options = ray_autoscaling_options
        self.max_concurrent_queries = max_concurrent_queries

        self.model_path = og_model_path
        self.application_name = og_model_string_parts[5]
        self.model_name = "_".join(og_model_string_parts[3].split("#")[:2])
        self.route_prefix = (
            f'/{self.model_name}/{og_model_string_parts[3].split("#")[3]}'
        )


def entry():
    parser = argparse.ArgumentParser()

    ray_actor_options = {
        "num_cpus": 1,
    }
    max_concurrent_queries = 10
    ray_autoscaling_options = {
        "target_num_ongoing_requests_per_replica": 7,
        "min_replicas": 0,
        "max_replicas": 5,
    }

    parser.add_argument(
        "--func", required=True, choices=["deploy", "undeploy"], help="deploy/undeploy"
    )
    parser.add_argument("--model", required=True, help="model path for the deployment")
    parser.add_argument(
        "--ray-actor-options",
        default=ray_actor_options,
        help="custom actor options for the deployment",
    )
    parser.add_argument(
        "--ray-autoscaling-options",
        default=ray_autoscaling_options,
        help="custom autoscaling options for the deployment",
    )
    args = parser.parse_args()

    model_config = InstillRayModelConfig(
        ray_actor_options=args.ray_actor_options,
        ray_autoscaling_options=args.ray_autoscaling_options,
        max_concurrent_queries=max_concurrent_queries,
        og_model_path=args.model,
    )

    return args.func, model_config
