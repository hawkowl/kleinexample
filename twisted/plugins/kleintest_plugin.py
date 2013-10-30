from twisted.application.service import ServiceMaker

serviceMaker = ServiceMaker(
    'kbn2', 'kbn2.service.view',
    'KBN Viewer', 'kbnview')
