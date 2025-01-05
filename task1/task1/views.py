from django.shortcuts import render
from .models import Buyer, Game


def create_data(request):
    buyer1 = Buyer.objects.create(name="Sasha", balance=500.00, age=17)  # Младше 18
    buyer2 = Buyer.objects.create(name="Maria", balance=600.00, age=25)    # Взрослый
    buyer3 = Buyer.objects.create(name="Michael", balance=800.00, age=30) # Взрослый

    game1 = Game.objects.create(title="Mario", cost=50.00, size=1.5, description="Весёлая игра", age_limited=False)  # Без ограничения по возрасту
    game2 = Game.objects.create(title="Witcher III", cost=50.00, size=2.0, description="Увлекательная история", age_limited=True)  # С ограничением по возрасту
    game3 = Game.objects.create(title="Phoenix Wright", cost=40.00, size=3.0, description="Незабываемый опыт", age_limited=True)  # С ограничением по возрасту

    game1.buyers.set([buyer2, buyer3])  # Game A без ограничения по возрасту
    game2.buyers.set([buyer2])            # Game B с ограничением по возрасту
    game3.buyers.set([buyer2])            # Game C с ограничением по возрасту

    return render(request, 'data_created.html')
