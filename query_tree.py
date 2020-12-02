import query



class QueryTree:

    def __init__(self):
        self.root = None
        self.cursor = None

    def getRoot(self):
        return self.root


    def _updateCursor(self, node):
        self.cursor = node




class ConditionalQuery:

    pass



class QueryCodes:

    # USE PANDAS DATAFRAME TO LIST CONDITIONS AND CALL AN INSTRUCTION
    # THE INSTRUCTION MAY BE FINAL, OR REFERENCE ANOTHER INSTRUCTION INSTRUCTIONS (FUNCTIONS)
    # INSTRUCTIONS MAY BE FINAL, OR REFERENCE ANOTHER INSTRUCTION (FUNCTION)

    # BRANCH CONDITIONS

    # CREATE A DAG WITH BINARY BRANCHING
    # IF TRUE, DO X; ELSE, DO Y

    # LIKELY/POSSIBLY RENAME CLASS
    # CONFIRM CREATION OF A DAG BEFORE RETURN IT AS AN OBJECT

    pass





class NodeCondition:

    def __init__(self):
        self._condition = None
        self._instruction = None



class QueryBranch:

    # (PLATNOIC) FINAL CAUSE FOR NODE
    self._node_condition = node_condition
    self._node_instruction = node_instruction
    # QUERY
    self._condition_stack = []
    self._instruction_stack = []

    def __init__(self, branch_condition, if_instruction, else_instruction=None):
        self._branch_condition = branch_condition
        self._if_instruction = if_instruction
        self._else_instruction = else_instruction

    def evaluate(self):

        # TODO: IF RESULT IS NOT NONE: RETURN RESULT, ELSE RAISE

        if self._branch_condition:
            return self._if_instruction
        else:
            return self._else_instruction




class Node:
    # TODO: NODE CLASS TO INHERIT FROM?
    pass



class QueryNode:

    def __init__(self, node_condition, node_instruction, parent_node):
        if parent_node:
            self._parent_node = parent_node
            self._is_root = False
        else:
            self._parent_node = None
            self._is_root = True
        self._children = []
        # (PLATNOIC) FINAL CAUSE FOR NODE
        self._node_condition = node_condition
        self._node_instruction = node_instruction
        # QUERY
        self._condition_stack = []
        self._instruction_stack = []
        self._query = None


    def _isRoot(self):
        return self._is_root

    def initQuery(self, prompt_text="Select an option: "):
        self._query = Query().setPrompt(prompt_text)
        return self

    def pushOption(self, option_condition, option_call, option_text):
        if option_condition:
            self._condition_stack.append(option_condition)
            self._instruction_stack.append(option_call)
            self._query.addOption(option_text)
        return self

    def _refreshNode(self):
        if self._node_condition:
            pass
        else:
            return

    def _buildQuery(self):
        if self._isRoot():
            # EXIT CODE
            pass
        else:
            # RETURN CODE
            pass

        self._query.build()
        return self

    def query(self):
        try:
            while True:
                query_selection = self._query.query()
                if len(query_selection) == 1:
                    break
                elif len(query_selection) > 1:
                    print("Too many options selected. Try again.")
                else:
                    print("No valid options selected")
        except ValueError as e:
            print(e)
            raise ValueError("Unable to query in node.")


    def getChildByOption(self, option):
        pass
