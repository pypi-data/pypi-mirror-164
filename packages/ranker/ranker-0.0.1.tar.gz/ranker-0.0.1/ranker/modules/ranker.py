from operator import itemgetter


class Ranker():
    """
    Processes results of games.

    Attributes:
        data : list[str]
            List of strings representing games results ["Team1 3, Team2 3", ...].
        points : dict[str: int]
            Dictionary with team name as key and points as value.
        ranking : list[(int, str)]
            List of tuples (points, team_name) representing the ranking in order.
    """

    def __init__(self, data: list[str] = []) -> None:
        self.data = data
        self.points = {}
        self.ranking = []


    def process_data(self) -> str:
        """
        Processes lines from stdin.

        The lines represent games results 
        in the following format: "team1_name 3, team1_name 3"

        It returns a str representing the ranking table.

        Returns
        -------
        str : str\n
            1. Tarantulas, 6 pts\n
            2. Lions, 5 pts\n
            3. FC Awesome, 1 pt\n
            4. Snakes, 1 pt\n
            5. Grouches, 0 pts\n
        
        Resulting ranking table
        """

        for line in self.data:
            #The followinf line returns a list of tuples: [(score, team1), (score, team2)]
            game = list(map(self.process_line, line.split(',')))

            if game[0][1] == game[1][1]:
                raise SameTeam("One or more teams are playing against themselves")

            if game[0][0] == game[1][0]:
                self.points[game[0][1]] += 1
                self.points[game[1][1]] += 1
            else:
                winner = max(game)
                self.points[winner[1]] += 3

        self.ranking = self.multisort(list(self.points.items()), ((0, False), (1, True)))
        return self.get_ranking()


    def get_ranking(self) -> str:
        """
        Returns ranking table as str.
        
        Returns
        -------
        table : str\n
            1. Tarantulas, 6 pts\n
            2. Lions, 5 pts\n
            3. FC Awesome, 1 pt\n
            4. Snakes, 1 pt\n
            5. Grouches, 0 pts\n
        
        Resulting ranking table
        """

        table = ''
        place = 1
        for team, points in self.ranking:
            p = 'pt' if points == 1 else 'pts' #
            table += f'{place}. {team}, {points} {p}\n'
            place += 1

        return table


    def process_line(self, line: str) -> tuple[int, str]:
        """
        Processes one line from stdin.
        
        Returns
        -------
        tuple : (int, str)
            (team_score, team_name)
        
        Returns tuple with team score and name
        """

        line = line.strip().split(' ')
        team_name = ' '.join(line[0:-1])
        team_score = int(line[-1])

        if team_name not in self.points:
            self.points[team_name] = 0
                
        return (team_score, team_name)
    

    def multisort(self, xs: list[tuple[str, int]], specs: list[tuple[int, bool]]) -> list[tuple[str, int]]: # Too much type hints?
        """
        Sorts list of tuples.

        Sorts list of tuples (str, int) by their first value in alphabetical order, 
        then sorts the list in descending order by their second value. After 
        the second sort the elements that have the same int value keep their 
        alphabetical order.

        Parameters
        ----------
        xs : list[(str, int)]
            List of tuples (points, team_name) representing the league ranking in order.
        specs : tuple(int, bool)
            Tuple with sorting specs.

        Returns
        -------
        xs : list[(str, int)]
            [(int, str), (int, srt), ...]

        Returns ordered list of tuples (points, team_name) representing the league ranking in order..
    
        """

        for key, reverse in specs:
            xs.sort(key=itemgetter(key), reverse=reverse)
        return xs


# Custom exceptions
class SameTeam(Exception):
    """ One or more teams are playing against themselves """
