from abc import ABC, abstractmethod


class DataContainer(ABC):
    '''An abstract class currently limited to retrieval and validation.'''
    @abstractmethod
    def getData(self):
        raise NotImplementedError

    #@abstractmethod
    #def setData(self, data):
    #    pass

    @abstractmethod
    def isValidContent(self, content):
        raise NotImplementedError


class OptionList(DataContainer):
    '''Currently a minimal wrapper to a list of OptionData objects.'''

    def __init__(self):
        self._options = []

    def getData(self):
        return self._options

    def isValidContent(self, content):
        if isinstance(content, OptionData):
            check_key_object, check_value_object = content.getData()
            for option in self._options:
                if (check_key_object == option.getOptionKey()):
                    raise ValueError("Pre-Existing Key: %s" % str(check_key_object))
                elif (check_value_object == option.getOptionValue()):
                    raise ValueError("Pre-Existing Value: %s" % str(check_value_object))
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

    def getOptionByKey(self, key_string):
        # print(key_string)
        for option in self._options:
            if key_string == option.getOptionKey().getData():
                return option
        raise KeyError("Key Not Found.")

    def __len__(self):
        return len(self._options)

    def _printOptions(self):
        for option in self._options:
            print(str(option))

    # SEARCH OPTION LIST FOR INPUT STRING
    def __contains__(self, object):
        if isinstance(object, OptionData):
            # SEARCH OPTION LIST FOR BOTH KEY AND TEXT
            return self._containsHelperOptionData(object)
        elif isinstance(object, OptionKey):
            return self._containsHelperOptionKey(object)
        elif isinstance(object, OptionValue):
            return self._containsHelperOptionValue(object)
        return False

    def _containsHelperOptionData(self, check_option):
        check_key_object, check_value_object = check_option.getData()
        has_key_data = self._containsHelperOptionKey(check_key_object)
        has_text_data = self._containsHelperOptionValue(check_value_object)
        return has_key_data and has_text_data

    def _containsHelperOptionKey(self, check_key_object):
        checking_string = str(check_key_object)
        for option in self._options:
            key_object, value_object = option.getData()
            if (checking_string == str(key_object)):
                return True
        return False

    def _containsHelperOptionValue(self, check_value_object):
        checking_string = str(check_value_object)
        for option in self._options:
            key_object, value_object = option.getData()
            if (checking_string == str(value_object)):
                return True
        return False


class OptionData:
    ''' Wrapper for Key-Value Pairs.'''
    # TODO: May update to be concrete class that descends from DataContainer.
    def __init__(self, key, value):
        try:
            if isinstance(key, str):
                self._key_object = OptionKey(key)
            elif isinstance(key, OptionKey):
                self._key_object = key
            else:
                raise TypeError("Neither a string nor OptionKey!")

            if isinstance(value, str):
                self._value_object = OptionValue(value)
            elif isinstance(value, OptionValue):
                self._value_object = value
            else:
                raise TypeError("Neither a string nor OptionValue!")

        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Invalid Option Data")


    def getOptionKey(self):
        return self._key_object

    def getOptionValue(self):
        return self._value_object

    def getData(self):
        return self.getOptionKey(), self.getOptionValue()

    def __str__(self):
        return str(self._key_object) + ") " + str(self._value_object)

    def __eq__(self, check_option_object):
        if isinstance(check_option_object, OptionData):
            check_key_object, check_value_object = check_option_object.getData()
            return ((self._key_object == check_key_object) and \
                    (self._value_object == check_value_object))
        return False


class OptionKey(DataContainer):
    ''' Wraps Key strings to follow requirements of OptionData objects.'''
    def __init__(self, key_string):
        try:
            if self.isValidContent(key_string):
                self._key_string = key_string
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Invalid Key Data.")

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
        return self._key_string

    def __eq__(self, key_object):
        if isinstance(key_object, OptionKey):
            return str(self) == str(key_object)
        return False



class OptionValue(DataContainer):
    ''' Wraps Value strings to follow requirements of OptionData objects.'''
    def __init__(self, value_string):
        try:
            if self.isValidContent(value_string):
                self._value_string = value_string
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Invalid Value Data")

    def getData(self):
        return str(self)

    def isValidContent(self, content):
        if isinstance(content, str):
            if content:
                return True
            else:
                raise ValueError("Empty Value String")
        else:
            raise TypeError("Not a String!")

    def __str__(self):
        return self._value_string

    def __eq__(self, text_data_obj):
        if isinstance(text_data_obj, OptionValue):
            return str(self) == str(text_data_obj)
        return False


class PromptStatement(DataContainer):
    ''' Wraps Prompt strings to follow requirements of Query objects.'''
    def __init__(self, prompt_string):
        try:
            if self.isValidContent(prompt_string):
                self._prompt_string = prompt_string
        except (ValueError, TypeError) as e:
            print(e)
            raise ValueError("Invalid Prompt Data")

    def getData(self):
        return str(self)

    def isValidContent(self, content):
        if isinstance(content, str):
            if content:
                return True
            else:
                raise ValueError("Empty Prompt String")
        else:
            raise TypeError("Not a String!")

    def __str__(self):
        return self._prompt_string
