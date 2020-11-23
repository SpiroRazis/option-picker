from abc import ABC, abstractmethod


class DataContainer(ABC):

    @abstractmethod
    def getData(self):
        pass

    #@abstractmethod
    #def setData(self, data):
    #    pass

    @abstractmethod
    def isValidContent(self, content):
        pass


class OptionList(DataContainer):

    def __init__(self):
        self._options = []

    def getData(self):
        return self._options

    def isValidContent(self, content):
        if isinstance(content, OptionData):
            check_selector_obj, check_text_obj = content.getData()
            for option in self._options:
                if (check_selector_obj == option.getSelectorData()):
                    raise ValueError("Pre-Existing Selector: %s" % str(check_selector_obj))
                elif (check_text_obj == option.getTextData()):
                    raise ValueError("Pre-Existing Text: %s" % str(check_text_obj))
            return True
        else:
            raise TypeError("Not an Option!")

    def addOption(self, option_object):
        try:
            if self.isValidContent(option_object):
                self._options.append(option_object)
                #self._addOptionHelper(option_object)
                # print("appended")
                # self._printOptions()
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Unable to Add Entry")

    def __len__(self):
        return len(self._options)

    def _printOptions(self):
        for option in self._options:
            print(str(option))

    # SEARCH OPTION LIST FOR INPUT STRING
    def __contains__(self, object):
        if isinstance(object, OptionData):
            # SEARCH OPTION LIST FOR BOTH SELECTOR AND TEXT
            return self._containsHelperOptionData(object)
        elif isinstance(object, SelectorData):
            return self._containsHelperSelectorData(object)
        elif isinstance(object, TextData):
            return self._containsHelperTextData(object)
        return False

    def _containsHelperOptionData(self, check_option):
        check_selector_data_obj, check_text_data_obj = check_option.getData()
        has_selector_data = self._containsHelperSelectorData(check_selector_data_obj)
        has_text_data = self._containsHelperTextData(check_text_data_obj)
        return has_selector_data and has_text_data

    def _containsHelperSelectorData(self, check_selector_data_obj):
        checking_string = str(check_selector_data_obj)
        for option in self._options:
            selector_data_obj, text_data_obj = option.getData()
            if (checking_string == str(selector_data_obj)):
                return True
        return False

    def _containsHelperTextData(self, check_text_data_obj):
        checking_string = str(check_text_data_obj)
        for option in self._options:
            selector_data_obj, text_data_obj = option.getData()
            if (checking_string == str(text_data_obj)):
                return True
        return False


class OptionData:

    def __init__(self, selector_string, text_string):
        try:
            self.selector_data_obj = SelectorData(selector_string)
            self.text_data_obj = TextData(text_string)
        except ValueError as e:
            print(e)
            raise ValueError("Invalid Option Data")

    def getSelectorData(self):
        return self.selector_data_obj

    def getTextData(self):
        return self.text_data_obj

    def getData(self):
        return self.getSelectorData(), self.getTextData()

    def __str__(self):
        return str(self.selector_data_obj) + ") " + str(self.text_data_obj)

    def __eq__(self, option_data_obj):
        if isinstance(option_data_obj, OptionData):
            check_selector_obj, check_text_obj = option_data_obj.getData()
            return ((self.selector_data_obj == check_selector_obj) and \
                    (self.text_data_obj == check_text_obj))
        return False


class SelectorData(DataContainer):

    def __init__(self, selector_string):
        try:
            if self.isValidContent(selector_string):
                self.selector = selector_string
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Invalid Selector Data")

    def getData(self):
        return str(self)

    def isValidContent(self, content):
        if isinstance(content, str):
            if content:
                for char in content:
                    if not (char.isalpha() or char.isdigit()):
                        raise ValueError("Invalid Character: %s" % char)
                return True
            else:
                raise ValueError("Empty String")
        else:
            raise TypeError("Not a String!")

    def __str__(self):
        return self.selector

    def __eq__(self, selector_data_obj):
        if isinstance(selector_data_obj, SelectorData):
            return str(self) == str(selector_data_obj)
        return False



class TextData(DataContainer):

    def __init__(self, text_string):
        try:
            if self.isValidContent(text_string):
                self.text = text_string
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Invalid Text Data")

    def getData(self):
        return str(self)

    def isValidContent(self, content):
        if isinstance(content, str):
            if content:
                return True
            else:
                raise ValueError("Empty Text Data")
        else:
            raise TypeError("Not a String!")

    def __str__(self):
        return self.text

    def __eq__(self, text_data_obj):
        if isinstance(text_data_obj, TextData):
            return str(self) == str(text_data_obj)
        return False
