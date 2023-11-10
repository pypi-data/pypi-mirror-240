from typing import Dict, Callable

from todotree.Task.Task import Task
from todotree.Config.TreePrint import TreePrint


class Tree:
    """
    Class representing a tree.

    The tree is a graph structure where there are no loops.
    However, this one is a special version of it.
    This tree is only 2 nodes deep.
    The leaves are the actual objects.
    The first layer of nodes consist of the value of one of the attributes of the leaves.
    Leaves with the same attribute are connected to the same node.

    To print the tree, simply cast it to string, like so `str(Tree())`.
    """

    def __init__(self, list_to_convert, key, **kwargs):
        """
        :param list_to_convert: the list to convert to a tree.
        :param key: the key of the first node in the tree.

        :param Optional arguments:
          - root_name: The display name of the root node.
          - empty_string: The display name of the "empty" or "default" first node.
          - config: The configuration file for printing the tree.
        """

        self.data_structure: Dict[str, list[Task]] = {}
        """
        The data structure of this tree.
        """

        self.root_name: str = kwargs.get("root_name", "root")
        """
        The name of the root of the tree.
        """

        self.empty_string: str = kwargs.get("empty_string", "default")
        """
        The 'empty' category.
        """

        self.treeprint: TreePrint = kwargs.get('treeprint', TreePrint("t", "l", "s", "e"))
        """
        The application configuration.
        """

        self.print_func: Callable[[str, Task], str] = kwargs.get('print_func', lambda key_value, task: str(task))
        """
        Function which prints the task.
        Input are: key_value: The value of the key given by `key`.
        Output must be a string.
        """

        # Generate tree.
        self.generate_tree(list_to_convert, key)

    @staticmethod
    def dict_add(dictionary, key, value):
        """
        Appends the item to the key if key exists, else creates the key with the item.
        :return:
        :param dictionary: The dictionary to mutate.
        :param key: The key.
        :param value: The value.
        :return: The mutated dictionary.
        """
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]
        return dictionary

    def generate_tree(self, list_to_parse: list, key: str):
        """
        Generate a tree like dictionary from the task list.
        The first line is each distinct key.
        Which points to a list of tasks.

        :key: The key to index to, such as due:date, project or context.
        :return: the generated Dictionary.
        """
        self.data_structure = {}  # Reset the data structure.
        for task in list_to_parse:
            task_attribute = getattr(task, key)
            if isinstance(task_attribute, list):
                if len(task_attribute) == 0:
                    self.dict_add(self.data_structure, self.empty_string, task)
                else:
                    for key_value in task_attribute:
                        self.dict_add(self.data_structure, key_value, task)
            else:
                # It is a single item.
                self.dict_add(self.data_structure, task_attribute if task_attribute else self.empty_string, task)

    def __str__(self):
        """
        Used for pretty printing the tree.
        """
        # Edge case: empty list -> empty string.
        if self.data_structure == {}:
            return ""

        return self.__outer_loop(self.root_name + "\n")

    def __outer_loop(self, return_string):
        """Construct the string over the dict."""
        len_first_node = len(self.data_structure)
        for i, first_node in enumerate(self.data_structure.keys()):
            first_list = self.data_structure[first_node]

            # Print the outer node. This prints the value of the key.
            return_string += self.treeprint.t_print if (i < len_first_node - 1) else self.treeprint.s_print
            # Section with the name of the first node.
            return_string += first_node + "\n"

            # Inner loop.
            return_string = self.__inner_loop(first_list, first_node, i, len_first_node, return_string)
        return return_string

    def __inner_loop(self, first_list, first_node, i, len_first_node, return_string):
        """Construct the string over the list."""
        first_line = self.treeprint.l_print if (i < len_first_node - 1) else self.treeprint.e_print
        len_second_node = len(first_list)
        for j, second_node in enumerate(first_list):
            # First node end of list
            second_line = self.treeprint.t_print if (j < len_second_node - 1) else self.treeprint.s_print
            # Line with the actual task.
            return_string += first_line + second_line + self.print_func(first_node, second_node) + "\n"
        return return_string
