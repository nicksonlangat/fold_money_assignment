import abc
from django.http import HttpResponse
from accounts.serializers import UserSerializer
from core.documents import HashtagDocument, ProjectDocument, UserDocument
from core.serializers import HashtagSerializer, ProjectSerializer
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class SearchProjectByUser(PaginatedElasticSearchAPIView):
    """
    * Search for projects created by a particular user

    * This API should return the project details, along with the hashtags
    * used in the project, and the details of the users that have created the project.
    """
    serializer_class = ProjectSerializer
    document_class = ProjectDocument

    def generate_q_expression(self, query):
        return Q('bool',
                 should=[
                     Q('match', user__name=query),
                     Q('match', user__email=query),
                 ], minimum_should_match=1)


class SearchProjectByHashtag(PaginatedElasticSearchAPIView):
    """
    * Search for projects that use specific hashtags

    * This API should return the project details, along with the hashtags 
    * used in the project, and the details of the users that have created the project.
    """
    serializer_class = ProjectSerializer
    document_class = ProjectDocument

    def generate_q_expression(self, query):
        return Q('bool',
                 should=[
                     Q('match', hashtags__name=query)
                 ], minimum_should_match=1)


class SearchProjectBySlugAndDescription(PaginatedElasticSearchAPIView):
    """
    * Full-text fuzzy search for projects

    * This API should allow fuzzy searching using the project slug and the description.
    * This API should return the hashtags used by the projects along with details of 
    the users that have created the project.
    """
    serializer_class = ProjectSerializer
    document_class = ProjectDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'slug',
                    'description'
                ], fuzziness='auto')


class SearchUsers(PaginatedElasticSearchAPIView):
    #Extra endpoint for searching users
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q('bool',
                 should=[
                     Q('match', name=query),
                     Q('match', email=query),
                 ], minimum_should_match=1)


class SearchHashtags(PaginatedElasticSearchAPIView):
    #Extra endpoint for searching hashtags
    serializer_class = HashtagSerializer
    document_class = HashtagDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'name',
                ], fuzziness='auto')
