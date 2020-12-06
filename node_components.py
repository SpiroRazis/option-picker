



class NodeData:
    '''Equivalent to a row in the Node Table'''
    def __init__(self, option_text, option_condition, option_instruction, children):

        self.option_text = option_text
        self.option_condition = option_condition
        self.option_instruction = option_instruction
        self.children = children

class NodeBlock:
    '''Does not require internal validity, but must be valid within table.'''
    pass

class NodeTable:
    '''An append-only table'''
    def isValidTable(self):
        pass

    def addNodeBlock(self, node_block):
        pass

    def _isValidNodeBlock(self, node_block):
        pass


############################################################

# TODO: CHILDREN SHOULD BE AN OPTION LIST?

class NodeOptionData(OptionData):

    def __init__(self, key_string, parent, node_data):
        try:
            super(OptionData, self).__init__(key_string, node_data.option_text)
        except ValueError as e:
            print(e)
            raise ValueError("Unable to instantiate base OptionData class.")

        self._parent_node = parent

        self._option_class = None
        self._condition = node_data.option_condition
        self._instruction = node_data.option_instruction
        self._children = node_data.children

    def getCondition(self):
        return self._condition

    def getInstruction(self):
        return self._instruction

    def getChildren(self):
        return self._children
