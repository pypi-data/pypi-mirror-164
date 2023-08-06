import json

from ordr.classes import Render, Server, Skin

class GetSkinRespond:
    def __init__(self, status, data) -> None:
        self.statusCode = status
        self.rawcontent = data
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            self.message = self._json["message"] if "message" in self._json else None
            self.maxSkins = self._json["maxSkins"] if "maxSkins" in self._json else None
            if "skins" in self._json:
                self.skins = []
                for i in self._json["skins"]:
                    self.skins.append(Skin.get_skin(i))

class CustomSkinRespond:
    def __init__(self, status, data) -> None:
        self.statusCode = status
        self.rawcontent = data
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            self.found = self._json["found"]
            self.removed = self._json["removed"]
            self.message = self._json["message"]
            if self.found == True:
                self.skinName = self._json["skinName"]
                self.skinAuthor = self._json["skinAuthor"]
                self.downloadLink = self._json["downloadLink"]


class GetRenderRespond:
    def __init__(self, status, data) -> None:
        self.statusCode = status
        self.rawcontent = data
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            self.maxRenders = self._json["maxRenders"] if "maxRenders" in self._json else None
            if "renders" in self._json:
                self.renders = []
                for i in self._json["server"]:
                    self.renders.append(Render(i))

class NewRenderRespond:
    def __init__(self, status, data) -> None:
        self.statusCode = status
        self.rawcontent = data
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            self.message = self._json["message"] if "message" in self._json else None
            self.renderID = self._json["renderID"] if "renderID" in self._json else None
            self.error = self._json["errorCode"] if "errorCode" in self._json else None
            self.reason = self._json["reason"] if "reason" in self._json else None

class GetServersRespond:
    def __init__(self, status, data) -> None:
        self.statusCode = status
        self.rawcontent = data
        try:
            self._json = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            self.message = data.decode("utf-8")
        else:
            if "servers" in self._json:
                self.servers = []
                for i in self._json["server"]:
                    self.servers.append(Server(i))