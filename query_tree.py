import query


class QueryCodes:

    pass



class QueryTree:


    def __init__(self):
        self.root = None
        self.cursor = None


    def getRoot(self):
        return self.root



    def _traverse(self, node):
        self.cursor = node





class QueryNode:

    def __init__(self, parent_node, primary_condition, primary_call):
        self._parent_node = parent_node
        self._primary_condition = primary_condition
        self._primary_call = primary_call
        self._condition_stack = []
        self._call_stack = []
        self._query = None
        self._children = []


    def _refreshNode(self):
        if self._primary_condition:
            pass
        else:
            return


    def _initQuery(self):
        self._query = Query().setPrompt("Select an Option:")

    def addCallOption(self, function_call, option_text):
        self._call_stack.append(function_call)
        self._query.addOption(option_text)
