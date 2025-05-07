from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer
from django.db.models import Sum, Count
from django.utils import timezone


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def create(self, request):
        data = request.data
        poll = Poll.objects.create(
            question=data['question'],
            pub_date=timezone.now(),
            active=True
        )
        
        choices = [
            Choice(poll=poll, choice_text=choice['choice_text'])
            for choice in data['choices']
        ]
        Choice.objects.bulk_create(choices)
        
        serializer = self.get_serializer(poll)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        poll = self.get_object()
        choice_id = request.data.get('choice_id')
        
        try:
            choice = poll.choices.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return Response({'status': 'vote recorded'})
        except Choice.DoesNotExist:
            return Response(
                {'error': 'Choice not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=['get'])
    def analytics(self, request):
        total_polls = Poll.objects.count()
        total_votes = Choice.objects.aggregate(total=Sum('votes'))['total'] or 0
        active_polls = Poll.objects.filter(active=True).count()
        
        polls_with_stats = Poll.objects.annotate(
            total_votes=Sum('choices__votes'),
            choice_count=Count('choices')
        ).values('id', 'question', 'total_votes', 'choice_count', 'pub_date')
        
        return Response({
            'total_polls': total_polls,
            'total_votes': total_votes,
            'active_polls': active_polls,
            'polls': polls_with_stats
        })

def index(request):
    return render(request, 'polls/index.html')

def create_poll(request):
    return render(request, 'polls/create.html')

def analytics_view(request):
    return render(request, 'polls/analytics.html')
