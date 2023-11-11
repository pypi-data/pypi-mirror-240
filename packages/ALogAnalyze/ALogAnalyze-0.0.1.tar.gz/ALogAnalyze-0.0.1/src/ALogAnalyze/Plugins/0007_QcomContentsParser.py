#!/usr/bin/env python3

from xml.dom.minidom import parse

class QcomContentsParser:

    """
    利用MediaPipe绘制手掌

    @data(template/contents.xml): QCOM contents.xml
    """

    def __init__(self, kwargs):
        pass

    def readXML(self, filePath, dnl_file):
        domTree = parse(filePath)
        rootNode = domTree.documentElement
        filePaths = []

        builds_flat = rootNode.getElementsByTagName("builds_flat")
        builds = builds_flat[0].getElementsByTagName("build")

        for build in builds:
            name = build.getElementsByTagName("name")[0].childNodes[0].data
            linux_root_path = build.getElementsByTagName("linux_root_path")
            download_files = build.getElementsByTagName(dnl_file)

            if (len(download_files) > 0):
                print(name + " >>>")
                filePaths.append(name + " >>>")

            for download_file in download_files:
                file_name = download_file.getElementsByTagName("file_name")
                file_paths = download_file.getElementsByTagName("file_path")
                # print(file_paths[0].childNodes[0].data + "/" + file_name[0].childNodes[0].data)
                outFilePath = linux_root_path[0].childNodes[0].data + file_paths[0].childNodes[0].data + file_name[0].childNodes[0].data
                print(outFilePath)

                filePaths.append(outFilePath)
        
        return filePaths

    def start(self, kwargs):
        data = kwargs["data"]

        return self.readXML(data, "download_file")

if __name__ == '__main__':
    pass
