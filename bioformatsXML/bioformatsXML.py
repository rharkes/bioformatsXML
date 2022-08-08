"""

"""
from pathlib import Path
import logging
import jpype.imports
import xmlschema
from jpype.types import *
import xml.etree.ElementTree as ET


class BioformatsXML:
    def __init__(self):
        # Launch the JVM
        jpype.startJVM(classpath=['jars/*'])
        logging.info('started JVM')
        from java.lang import System
        logging.info(f'Java classpath: {System.getProperty("java.class.path")}')
        from loci.formats import ImageReader
        from loci.formats import MetadataTools
        from loci.common import DebugTools
        from loci.formats import UnknownFormatException
        from java.lang import RuntimeException
        logging.info('Java import complete')
        DebugTools.setRootLevel("ERROR")
        self.UnknownFormatException = UnknownFormatException
        self.RuntimeException = RuntimeException
        self.MetadataTools = MetadataTools
        self.reader = ImageReader()
        self.my_schema = xmlschema.XMLSchema(r'xml_schema/ome.xsd')
        logging.info('Class loaded')

    def get_xml(self, inputFile):
        if not Path(inputFile).exists():
            logging.info(f'File {inputFile} not found')
            raise FileNotFoundError
        try:
            logging.info(f'File {inputFile} found')
            if self.reader.getCurrentFile():
                logging.info(f'Closing {self.reader.getCurrentFile()}')
                self.reader.close()
            omeMeta = self.MetadataTools.createOMEXMLMetadata()
            self.reader.setMetadataStore(omeMeta)
            self.reader.setId(str(inputFile))
            xmlstring = omeMeta.dumpXML()
            root = ET.fromstring(str(xmlstring))
            tree = ET.ElementTree(root)
            return tree
        except (self.UnknownFormatException) as ex:
            logging.info(f'File {inputFile} not bioformats compatible.')
            return None
        except (self.RuntimeException) as ex:
            logging.info(f'File {inputFile} runtime exception:{ex.stacktrace()}')
            return None

    def verify_schema(self, xmlfile):
        return self.my_schema.is_valid(xmlfile)
