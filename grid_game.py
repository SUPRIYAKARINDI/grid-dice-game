import random
class Player:
    def __init__(self, player_id, rolls):
        self.player_id = player_id
        self.rolls = [random.randint(1,6)]
        self.position = 0
        self.dice_history = []
        self.position_history = []

    def move(self, step, max_position):
        self.dice_history.append(step)
        if self.position + step <= max_position:
            self.position += step
            self.position_history.append(self.position)
            return True
        else:
            self.position_history.append(self.position)  
            return False


class GridGame:
    def __init__(self):
        self.players = [
            Player(1, [random.randint(1,6)]),   
            Player(2, [random.randint(1,6)]),   
            Player(3, [random.randint(1,6)])   
        ]
        
    def reset_player(self, player):
        player.position = 0
        player.position_history.append(player.position)

    def play(self, grid_number):
        max_position=grid_number*grid_number
        print(f"grid_number:{grid_number}")
        print(f"max_position:{max_position}")
        Winner=False
        round_index=0
        while not Winner:
            # roll=random.randint(1,6)
            # print(f"dice_value:{roll}")
            print(f"\n--- Round {round_index + 1} ---")
            for player in self.players:
                roll=random.randint(1,6)
                print(f"dice_value:{roll}")
               
                current_pos = player.position
                remaining = max_position - current_pos
                if roll > remaining:
                    print(f"Player {player.player_id} rolled {roll} but only {remaining} steps left — invalid move.")
                    player.dice_history.append(roll)
                    player.position_history.append(current_pos)
                    continue
                moved = player.move(roll,max_position)
                print(f" Player {player.player_id} rolled {roll}, moved from {current_pos} to {player.position}")
                if player.position==max_position:
                    print("\n--- Final Results ---")
                    print(f"Player {player.player_id} | Rolls: {player.dice_history} | Positions: {player.position_history} | Winner: {player.position}")
                    print(f"Player{player.player_id} is the Winner")
                    Winner=True
                for player in self.players:
                    print(f"Player {player.player_id} | Rolls: {player.dice_history} | Positions: {player.position_history} | Final: {player.position}")
                for other in self.players:
                    if other != player and other.position == player.position and other.position != 0:
                        print(f"Player {player.player_id} cuts Player {other.player_id} at position {player.position}!")
                        self.reset_player(other)
            round_index=round_index+1
            # Winner= game.show_results(max_position)
           

    def show_results(self,max_pos): 
        for p in self.players:
            if p.position==max_pos:
                print("\n--- Final Results ---")
                print(f"Player {p.player_id} | Rolls: {p.dice_history} | Positions: {p.position_history} | Winner: {p.position}")
                print(f"Player{p.player_id} is the Winner")
                return True
            else:
                print(f"Player {p.player_id} | Rolls: {p.dice_history} | Positions: {p.position_history} | Final: {p.position}")
                return False
     


if __name__ == "__main__":
    game = GridGame()
    game.play(7)
    # game.show_results()

