class Player:
    def __init__(self, family_name, first_name, date_of_birth, chess_national_id):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.chess_national_id = chess_national_id

    def serialize_player_data(self):
        serialized_data = {
            "Family_name": self.family_name,
            "First_name": self.first_name,
            "Date_of_birth": self.date_of_birth,
            "Chess_national_id": self.chess_national_id,
        }
        return serialized_data
