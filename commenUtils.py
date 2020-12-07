import logging

logger = logging.getLogger(__name__)


def get_input_data(input_file_name: str) -> dict[str, list[(int, str)]]:
    f = open(input_file_name, "r")
    bag_connection_dict: dict[str, list[(int, str)]] = dict()
    key: str
    values: str
    bag: str
    for line in f:
        key, values = line.strip().split("contain")
        key = key.replace("bags", "").strip()
        logger.debug(key)
        bag_connection_dict[key] = []
        if "no" not in values:
            for value in values.split(","):
                bag = value.strip()[1:].replace("bags", "").replace("bag", "").replace(".", "").strip()
                bag_connection_dict[key].append((int(value.strip()[0]), bag))
    f.close()
    return bag_connection_dict
