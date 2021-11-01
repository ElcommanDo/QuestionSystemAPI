from rest_framework import generics, status
from .serializers import QuestionSerializer, AnswerSerializer
from question.models import Question, Answer
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class AnswerListView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_sulg = self.kwargs.get('slug')
        question = Question.objects.get(slug=kwarg_sulg)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError('You are answered this question before')
        serializer.save(author=self.request.user, question=question)


class AnswerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = QuestionSerializer


class QuestionAnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        kwargs_slug = self.kwargs.get('slug')
        answers = Answer.objects.filter(question__slug=kwargs_slug).order_by('-created_at')
        print(kwargs_slug)
        return answers


class AnswerLike(APIView):
    # seriaizer_class = AnswerSerializer

    def post(self, request, pk):
        answer = Answer.objects.get(id=pk)
        answer.voters.add(request.user)
        answer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        answer = Answer.objects.get(id=pk)
        answer.voters.remove(request.user)
        answer.save()
        return Response(status=status.HTTP_200_OK)

    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


