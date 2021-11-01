from rest_framework import serializers
from question.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_voted = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        exclude = ['question', 'voters', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d %Y')

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get('request')
        return instance.voters.filter(pk=request.user.pk).exists()


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    user_answer = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answer_count = serializers.SerializerMethodField(read_only=True)
    answers = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        exclude = ['updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d %Y')

    def get_user_answer(self, instance):
        request = self.context.get('request')
        return instance.answers.filter(author=request.user).exists()

    def get_answer_count(self, instance):
        return instance.answers.count()

