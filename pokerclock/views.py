from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.http import require_POST
from django.views import generic
from .models import Tournament

def create_game(request):
    return render(request, 'pokerclock/create.html')

@require_POST
def start_game(request):
	error = None

	#first checking for errors

	if len(request.POST.get('game-type')) == 0:
		error = "Field 'Game type' cannot be empty"

	for el in request.POST.get('blinds-structure').split(","):
		try:
			x = int(el)
		except ValueError:
			error = "You should write big blinds in a row, separated by a comma, like this: 50,100,200,300 ..."

	check_payouts = []
	for payout in request.POST.get('payouts-scheme').split(","):
		check_payouts.append(int(payout))

	if sum(check_payouts)!=100:
		error = "Prizes sum needs to be 100%% (current is %d%%)"%sum(check_payouts)

	try:
		TL_test = int(request.POST.get('time-level'))
	except:
		error = "Level time must be an integer and cannot be empty"

	explanation = {'error_description':error}
	if error != None:
		return render_to_response('pokerclock/error.html',explanation)

	#stop checking for errors and suppose a tournament can be created

	currency = " " + request.POST.get('currency')
	number_of_players = len(request.POST.get('player-names').split(','))

	if request.POST.get('bet-limit') == "(Not specified)":
		bets = ''
	else:
		bets = request.POST.get('bet-limit')+" "

	game_type = request.POST.get('buy-in') + currency + " [" + bets + request.POST.get('game-type') + "]"
	if request.POST.get('rebuys')=='Yes':
		game_type+=' R/A'
	else:
		game_type+=' Freezeout'

	if request.POST.get('KO')=='1':
		game_type+=', Knockout '+ request.POST.get('KO-price') + currency
	elif request.POST.get('KO')=='2':
		game_type+=', Progressive Knockout ' + request.POST.get('KO-price') + currency+", (KO payout = %s%%)"%request.POST.get('KO-share')

	return render_to_response('pokerclock/game.html',
		{
		 'game_type': game_type,
		 'structure': request.POST.get('blinds-structure'),
		 'start_stack': request.POST.get('start-stack'),
		 'limit': request.POST.get('time-level'),
		 'buy_in': request.POST.get('buy-in'),
		 'players': request.POST.get('player-names'),
		 'payouts': request.POST.get('payouts-scheme'),
		 'total_players': number_of_players,
		 'rebuy_game': request.POST.get('rebuys'),
		 'rebuy_price': request.POST.get('rebuy-price'),
		 'rebuy_chips': request.POST.get('rebuy-chips'),
		 'rebuy_stop': request.POST.get('rebuy-stop'),
		 'addon_game': request.POST.get('rebuys'),
		 'addon_price': request.POST.get('addon-price'),
		 'addon_chips': request.POST.get('addon-chips'),
		 'KO_type': request.POST.get('KO'),
		 'KO_price': request.POST.get('KO-price'),
		 'KO_share': request.POST.get('KO-share'),
		 'currency': request.POST.get('currency'),
		 })