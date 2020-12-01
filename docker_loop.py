from datetime import datetime as dt

import docker
import pprint as pp
import query
import subprocess
import sys



class DockerLoop:

    _RETURN_VALUE = "RETURN"

    def __init__(self):
        self._client = None
        self._subprocess = None
        self._user_query = None
        self._eligible_func_dict = {}
        self._imageSearchHistory = []

    #def setup():
    #    self._connectClient()

    def connectClient(self):
        self._client = docker.from_env()

    def disconnectClient(self):
        self._client.close()
        self._client = None

    def looper(self):
        if self._client:
            pass
        else:
            raise RuntimeError("Client not connected.")
        pass

    def _hasImages(self):
        return (len(self._client.images.list()) > 0)

    def _hasContainers(self):
        return (len(self._client.containers.list()) > 0)


    def _estabishAvailableOptions(self):
        self._newQuery()
        self._addImageOptions()
        self._addContainerOptions()

        self._user_query.build()



    def _newQuery(self):
        self._user_query = Query()
        self._eligible_func_dict = {}

    def _clearQuery(self):
        self._user_query = None
        self._eligible_func_dict = {}


    def _updateQuery(self, func_option, func_reference):
        self._user_query.addOption(func_option)
        self._eligible_func_dict[func_option] = func_reference

    def _executeQuery():
        pass


    def _addImageOptions(self):
        if self._hasImages():
            self._updateQuery("", self._____)

        self._updateQuery("Search", self._dHubImageSearch())


        # OTHER IMAGES:


        # EXISTING IMAGE ACTIONS

        # SEARCH FOR IMAGE(S) IS ALWAYS AVAILABLE

        # RETURN IS ALWAYS AVAILABLE - UNLESS EXIT

        # _. BUILD? - IF DOCKERFILE AVAILABLE
        # _. RUN? - IF IMAGE AVAILABLE
        # _. RM? - REMOVE CONTAINER - REQUIRES CONTAINER
        # _. RMI? - IF IMAGE AVAILABLE

        # SEARCH

    def _addContainerOptions(self):
        if self._hasContainers():
            self._updateQuery("", self.___)



    ################################################################
    '''
        SEARCH DOCKER HUB FOR AN IMAGE
    '''
    def _dHubImageSearch(self):
        try:
            print("Enter a search term: ")
            search_term = input("-->")
            response = self._client.images.search(search_term)
            # EXPECT A LIST OF DICTS
            self._updateSearchHistory(search_term, response)
            pp.pprint(response)
        except docker.errors.APIError as e:
            print(e)


    def _updateSearchHistory(self, search_term, response):
        # COULD UPDATE TO ADD THE SEARCH OPTIONS?
        self._imageSearchHistory.append({"time_stamp": dt.now(), \
                                        "search_term": search_term, \
                                        "response": response})

    ################################################################

    def _selectClientImage(self):
        image_query = Query().setPrompt("Images:")
        for image in self._client.images.list():
            image_query.addOption(image)
        image_query.addOption(self._RETURN_VALUE)
        image_query.build()
        return image_query.query()

    def _selectorActions(self):
        pass


    def _containerOptions(self):
        container_query = Query().setPrompt("Containers:")
        for container in self._client.containers.list():
            container_query.addOption(container)
        container_query.build()
        return container_query.query()


    # TODO: PLACEHOLDER/TENTATIVE FUNCTIONS, MAY BE REMOVED

    # NEED TO DOCKER BUILD
    def docker_build():

        return

    # NEED TO RUN DOCKER FILE
    def docker_run():

        return

    # NEED TO REMOVE CONTAINER(S)
    def docker_rm():

        return

    # NEED TO REMOVE IMAGE(S)

    def docker_rmi():

        return



if __name__ == "__main__":
    d_loop = DockerLoop()
    d_loop.connectClient()
    d_loop.disconnectClient()

    sys.exit(0)

sys.exit(0)
