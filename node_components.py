from abc import ABC, abstractmethod
from query_components import OptionList, OptionData, OptionKey, OptionValue, PromptStatement



class QueryNode(ABC):

    def __init__(self):
        self._reference = None
        self._parent = None
        # THIS OBJECT AS AN AGENT. MAYBE USE AN AGENT-NODE INTERFACE?
        self._possible_objects = None
        self._possible_verbs = None
        self._children = None
        self._eligibility = None

        self._query = None
        self._option_value = None
        self._prompt = None

        self._max_selectable = None

    ########################################
    def setReference(self, reference):
        self._reference = reference

    def getReference(self):
        return self._reference
    ########################################
    def setParent(self, parent):
        self._parent = parent

    def getParent(self):
        return self._parent
    ########################################
    def setPossibleObjects(self, possible_objects):
        self._possible_objects = possible_objects

    def getPossibleObjects(self):
        return self._possible_objects
    ########################################
    def setPossibleVerbs(self, possible_verbs):
        self._possible_verbs = possible_verbs

    def getPossibleVerbs(self):
        return self._possible_verbs
    ########################################
    def setChildren(self, children):
        self._children = children

    def getChildren(self):
        return self._children
    ########################################
    def setOptionValue(self, option_value):
        try:
            self._option_value = OptionValue(option_value)
        except ValueError as e:
            print(e)
            raise ValueError("Unable to set option value.")

    def getOptionValue(self):
        return self._option_value
    ########################################
    def setPrompt(self, prompt):
        try:
            self._prompt = PromptStatement(prompt)
        except ValueError as e:
            print(e)
            raise ValueError("Unable to set prompt statement.")

    def getPrompt(self):
        return self._prompt
    ########################################
    def setMaxSelectable(self, max_selectable):
        self._max_selectable = max_selectable

    def getMaxSelectable(self):
        return self._max_selectable
    ########################################
    @abstractmethod
    def establishEligibility(self):
        raise NotImplementedError

    def getEligibility(self):
        return self._eligibility
    ########################################
    @abstractmethod
    def generateQuery(self):
        raise NotImplementedError

    @abstractmethod
    def executeQuery(self):
        raise NotImplementedError
    ########################################
    @abstractmethod
    def executeMethod(self):
        raise NotImplementedError
    ########################################
    @abstractmethod
    def refresh(self):
        # FORMERLY UPDATE
        raise NotImplementedError
