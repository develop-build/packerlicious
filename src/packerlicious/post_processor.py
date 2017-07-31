from . import BasePackerObject
import validator


class PackerPostProcessor(BasePackerObject):

    def __init__(self, title=None, **kwargs):
        super(PackerPostProcessor, self).__init__(title, **kwargs)


class DockerImport(PackerPostProcessor):
    """
    Docker Import Post-Processor
    https://www.packer.io/docs/post-processors/docker-import.html
    """
    resource_type = "docker-import"

    props = {
        'repository': (basestring, True),
        'tag': (basestring, False),
    }


class DockerPush(PackerPostProcessor):
    """
    Docker Push Post-Processor
    https://www.packer.io/docs/post-processors/docker-push.html
    """
    resource_type = "docker-push"

    props = {
        'aws_access_key': (basestring, False),
        'aws_secret_key': (basestring, False),
        'aws_token': (basestring, False),
        'ecr_login': (validator.boolean, False),
        'login': (validator.boolean, False),
        'login_email': (basestring, False),
        'login_username': (basestring, False),
        'login_password': (basestring, False),
        'login_server': (basestring, False),
    }


class DockerSave(PackerPostProcessor):
    """
    Docker Save Post-Processor
    https://www.packer.io/docs/post-processors/docker-save.html
    """
    resource_type = "docker-save"

    props = {
        'path': (basestring, True),
    }


class DockerTag(PackerPostProcessor):
    """
    Docker Tag Post-Processor
    https://www.packer.io/docs/post-processors/docker-tag.html
    """
    resource_type = "docker-tag"

    props = {
        'repository': (basestring, True),
        'tag': (basestring, False),
        'force': (basestring, False),
    }


class GoogleComputeExport(PackerPostProcessor):
    """
    Google Compute Image Exporter Post-Processor
    https://www.packer.io/docs/post-processors/googlecompute-export.html
    """
    resource_type = "googlecompute-export"

    props = {
        'paths': ([basestring], True),
        'keep_input_artifact': (validator.boolean, False),
    }


class Manifest(PackerPostProcessor):
    """
    Manifest Post-Processor
    https://www.packer.io/docs/post-processors/manifest.html
    """
    resource_type = "manifest"

    props = {
        'output': (basestring, False),
        'strip_path': (validator.boolean, False),
    }
