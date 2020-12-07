from commenUtils import get_input_data
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--log", default="info")

options = parser.parse_args()
levels = {'info': logging.INFO, 'debug': logging.DEBUG}

level = levels.get(options.log.lower())

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    level=level)

logger = logging.getLogger(__name__)


def invert_dict(bag_connection_list: dict[str, list[(int, str)]]) -> dict[str, set[str]]:
    key: str
    values: str
    bag: str
    rev_bag_connection: dict[str, set[str]] = dict()
    for bag_col in bag_connection_list:
        logger.debug(f"Connection: {bag_col} -> {bag_connection_list[bag_col]}")
        keys = bag_connection_list[bag_col]
        for key in keys:
            if key[1] not in rev_bag_connection:
                rev_bag_connection[key[1]] = {bag_col}
            else:
                rev_bag_connection[key[1]].add(bag_col)
    return rev_bag_connection


def solution_part_1(file_name: str) -> int:
    bag_connections: dict[str, list[(int, str)]] = get_input_data(file_name)
    rev_bag_connections: dict[str, set[str]] = invert_dict(bag_connections)
    for conn in rev_bag_connections:
        logger.debug(f"Key: {conn}, vales: {rev_bag_connections[conn]}")
    backlog: list[str] = list(rev_bag_connections["shiny gold"])
    visited: set[str] = {"shiny gold"}
    current_col: str
    while len(backlog) != 0:
        current_col = backlog.pop(0)
        visited.add(current_col)
        if current_col in rev_bag_connections:
            backlog.extend(rev_bag_connections[current_col])
    return len(visited)-1


def solution_part_2(file_name: str) -> int:
    bag_connections: dict[str, list[(int, str)]] = get_input_data(file_name)
    backlog: list[(int, str)] = list(bag_connections["shiny gold"])
    current_bag: (int, str)
    bags_needed: int = 0
    while len(backlog) != 0:
        current_bag = backlog.pop(0)
        bags_needed += current_bag[0]
        backlog.extend(multiply_connections(current_bag[0], bag_connections[current_bag[1]]))
    return bags_needed


def multiply_connections(factor: int, connections: list[(int, str)]) -> list[(int, str)]:
    multiplied_connections: list[(int, str)] = []
    for connection in connections:
        multiplied_connections.append((connection[0]*factor, connection[1]))
    return multiplied_connections


if __name__ == '__main__':
    logger.info(solution_part_1("inputData.txt"))
    logger.info(solution_part_2("inputData.txt"))
