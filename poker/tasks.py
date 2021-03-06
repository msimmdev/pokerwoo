from background_task import background
from decimal import Decimal
from . import models


@background()
def create_stats(player_ref, competition):
    games = models.CompetitionGame.objects.filter(competition=competition)
    competition_object = models.Competition.objects.get(pk=competition)
    stats = models.Stats.objects.filter(
        player_ref=player_ref, competition=competition)
    statable_games = 0

    if len(stats) == 1:
        stat_object = stats[0]
    else:
        stat_object = models.Stats(
            player_ref=player_ref, competition=competition_object)

    stat_object.games_played = 0
    stat_object.games_won = 0
    stat_object.place_1 = 0
    stat_object.place_2 = 0
    stat_object.place_3 = 0
    stat_object.times_placed = 0
    stat_object.net_winnings = 0
    stat_object.average_placing = 0
    stat_object.average_rating = 0
    stat_object.score = 0
    stat_object.new_score = 0
    stat_object.win_rate = 0
    stat_object.place_rate = 0
    stat_object.gain_per_game = 0

    sum_placing = 0
    sum_rating = 0

    for competition_game in games:
        participations = models.GameParticipant.objects.filter(
            player_ref=player_ref, game=competition_game.game)
        if (participations):
            participant = participations[0]
            game = competition_game.game
            if game.complete:
                stat_object.games_played = stat_object.games_played + 1
                player_list = models.GameParticipant.objects.filter(game=game)

                max_place = 0
                split1 = 0
                split2 = 0
                split3 = 0
                for player in player_list:
                    if player.place > max_place:
                        max_place = player.place
                    if player.place == 1:
                        split1 = split1 + 1
                    if player.place == 2:
                        split2 = split2 + 1
                    if player.place == 3:
                        split3 = split3 + 1
                    if player.place == 0:
                        game.scorable = False

                if game.scorable:
                    stat_object.score = stat_object.score + \
                        (len(player_list) - participant.place) + 1
                    sum_placing = sum_placing + participant.place
                    sum_rating = sum_rating + \
                        (max_place / 2) - participant.place
                    statable_games = statable_games + 1

                    winner_score = len(player_list) * 6
                    second_score = round(len(player_list) * 2.5)

                    if len(player_list) <= 2:
                        score_stake = 12
                        score_place = 1
                    elif len(player_list) == 3:
                        score_stake = 9
                        score_place = 1
                    elif len(player_list) == 4:
                        score_stake = 8
                        score_place = 1
                    elif len(player_list) == 5:
                        score_stake = 14
                        score_place = 2
                    elif len(player_list) == 6:
                        score_stake = 13
                        score_place = 2
                    elif len(player_list) == 7:
                        score_stake = 12
                        score_place = 2
                    elif len(player_list) == 8:
                        score_stake = 16
                        score_place = 3
                    elif len(player_list) == 9:
                        score_stake = 15
                        score_place = 3
                    elif len(player_list) >= 10:
                        score_stake = 14
                        score_place = 3

                    score_pot = score_stake * (len(player_list) - score_place)
                    
                    if participant.place == 1:
                        stat_object.new_score = stat_object.new_score + winner_score
                    elif participant.place == 2 and score_place == 2:
                        stat_object.new_score =  stat_object.new_score + score_pot - winner_score
                    elif participant.place == 2 and score_place == 3:
                        stat_object.new_score = stat_object.new_score + second_score
                    elif participant.place == 3 and score_place == 3:
                        stat_object.new_score = stat_object.new_score + score_pot - winner_score - second_score
                    else:
                        stat_object.new_score = stat_object.new_score - score_stake


                if participant.place == 1:
                    if split1 > 0:
                        pot = game.stake * \
                            len(player_list) - game.stake * game.place_two_multiplier - \
                            game.stake * game.place_three_multiplier
                        stat_object.net_winnings = stat_object.net_winnings + \
                            Decimal((pot / split1) - game.stake)
                    stat_object.games_won = stat_object.games_won + 1
                    stat_object.place_1 = stat_object.place_1 + 1
                    stat_object.times_placed = stat_object.times_placed + 1
                elif participant.place == 2 and game.place_two_multiplier > 0:
                    if split2 > 0:
                        pot = game.stake * game.place_two_multiplier
                        stat_object.net_winnings = stat_object.net_winnings + \
                            Decimal((pot / split2) - game.stake)
                    stat_object.place_2 = stat_object.place_2 + 1
                    stat_object.times_placed = stat_object.times_placed + 1
                elif participant.place == 3 and game.place_three_multiplier > 0:
                    if split3 > 0:
                        pot = game.stake * game.place_three_multiplier
                        stat_object.net_winnings = stat_object.net_winnings + \
                            Decimal((pot / split3) - game.stake)
                    stat_object.place_3 = stat_object.place_3 + 1
                    stat_object.times_placed = stat_object.times_placed + 1
                else:
                    stat_object.net_winnings = stat_object.net_winnings - \
                        Decimal(game.stake)

    if stat_object.games_played > 0:
        if sum_placing > 0:
            stat_object.average_placing = sum_placing / statable_games
        if sum_rating > 0:
            stat_object.average_rating = sum_rating / statable_games
        stat_object.win_rate = (
            stat_object.games_won / stat_object.games_played)
        stat_object.place_rate = (
            stat_object.times_placed / stat_object.games_played)
        stat_object.gain_per_game = (
            stat_object.net_winnings / stat_object.games_played)
        stat_object.save()

        c_part = models.CompetitionParticipant.objects.filter(competition=competition_object, player_ref=player_ref)
        if not c_part:
            p_object = models.CompetitionParticipant(
                competition=competition_object, player_ref=player_ref)
            p_object.save()
    else:
        c_part = models.CompetitionParticipant.objects.filter(competition=competition_object, player_ref=player_ref)
        if c_part:
            c_part.delete()
