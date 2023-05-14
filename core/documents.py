from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from accounts.models import UserAccount
from .models import Hashtag, Project

@registry.register_document
class UserDocument(Document):
    id = fields.IntegerField()
    class Index:
        name = "users"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = UserAccount
        fields = [
            "email",
            "name",
            "date_joined",
            "is_superuser",
            "is_staff",
            "is_active"
        ]


@registry.register_document
class HashtagDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = "hashtags"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Hashtag
        fields = [
           "name",
           "created_at",
        ]


@registry.register_document
class ProjectDocument(Document):
    id = fields.IntegerField()
    user = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "email": fields.TextField(),
        "name": fields.TextField(),
        "is_superuser": fields.BooleanField(),
        "is_staff": fields.BooleanField(),
        "is_active": fields.BooleanField()
    })
    hashtags = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "name": fields.TextField(),
        "created_at": fields.TextField(),
    })

    class Index:
        name = "projects"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Project
        fields = [
            "name",
            "slug",
            "description",
            "created_at",
        ]
