from query_components import OptionList, OptionData, SelectorData, TextData

class Query:

    def __init__(self):
        self._input_symbol = "-->"
        self._prompt = None
        self._option_list = None
        self._is_built = False
        self._input_string = ""
        self._input_list = None
        self._validated_input_list = None
        self._query_return = None

    # PUBLIC ##########################
    def query(self):
        if self._is_built:
            try:
                self._executeQuery()
                return self._query_return
            except ValueError as e:
                print(e)
                raise ValueError("Unable to Query")
        else:
            raise ValueError("Not Built")

    # SET ##########################
    def setPrompt(self, text):
        if self._is_built:
        # TODO: VALIDATE PROMPT
            raise ValueError("Already Built")
        else:
            self._prompt = TextData(text)
            return self

    # ADD ##########################
    def addOption(self, selector_string, text_string):
        if self._is_built:
        # TODO: VALIDATE PROMPT
            raise ValueError("Already Built")
        else:
            if not self._option_list:
                self._option_list = OptionList()
            try:
                self._option_list.addOption(OptionData(selector_string, text_string))
                return self
            except ValueError as e:
                print(e)
                raise ValueError("Unable to Add Option")

    # TODO:
    # ADD AN AUTO-OPTION: NUMERIC OPTION
    # USE AN ITERATOR OBJECT TO RETRIEVE UPDATED NUMBER VIA YIELD





    # FINALIZE ##########################
    def build(self):
        if self._is_built:
            raise ValueError("Already Built")
        else:
            if self._prompt and self._option_list and (len(self._option_list) > 0):
                self._is_built = True
                return self
            else:
                raise ValueError("Incomplete Query Build")

    # QUERY ##########################
    def _executeQuery(self):
        self._clearInputFields()
        self._clearQueryReturn()
        self._printPrompt()
        self._printOptions()
        try:
            self._requestInput()
            self._parseInput()
            self._validateInput()
            self._collapseInputRepeats()
            self._updateQueryReturn()
            self._clearInputFields()
        except ValueError as e:
            print(e)
            self._clearInputFields()
            raise ValueError("Invalid Query")

    #####################################
    def _clearInputFields(self):
        self._clearInputString()
        self._clearInputList()
        self._clearValidatedInputList()

    def _clearInputString(self):
        self._input_string = ""

    def _clearInputList(self):
        self._input_list = []

    def _clearValidatedInputList(self):
        self._validated_input_list = []

    def _clearQueryReturn(self):
        self._query_return = []

    #####################################
    def _printPrompt(self):
        print(str(self._prompt))

    def _printOptions(self):
        self._option_list._printOptions()

    def _requestInput(self):
        self._input_string = input(self._input_symbol).strip()

    def _parseInput(self):
        if self._input_string:
            self._input_list = self._input_string.split()
        else:
            raise ValueError("Empty String")

    def _validateInput(self):
        if self._input_list:
            try:
                for string in self._input_list:
                    if SelectorData(string) in self._option_list:
                        self._validated_input_list.append(string)
                    else:
                        raise ValueError("Provided input not amongst options")
            except ValueError as e:
                print(e)
                raise ValueError("Invalid Input: %s" % string)
        else:
            raise ValueError("Empty List")

    def _collapseInputRepeats(self):
        self._validated_input_list.sort()
        collapsed_input = []
        for valid_input_string in self._validated_input_list:
            if collapsed_input:
                if valid_input_string != collapsed_input[-1]:
                    collapsed_input.append(valid_input_string)
            else:
                collapsed_input.append(valid_input_string)
        self._validated_input_list = collapsed_input

    def _updateQueryReturn(self):
        self._query_return = self._validated_input_list
