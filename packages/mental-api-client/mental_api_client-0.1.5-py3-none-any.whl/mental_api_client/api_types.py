from datetime import datetime

from base import APIObject


class Team(APIObject):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, data):
        if data:
            return cls(
                id=data['id'],
                name=data['name']
            )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name
        )


class Survey(APIObject):
    def __init__(self, id, start_date, end_date, team_id):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.team_id = team_id

    @classmethod
    def from_dict(cls, data):
        if data:
            start_date = data['start_date']
            end_date = data['end_date']

            return cls(
                id=data['id'],
                start_date=start_date and datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ"),
                end_date=end_date and datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ"),
                team_id=data['team_id']
            )

    def to_dict(self):
        return dict(
            id=self.id,
            start_date=self.start_date and self.start_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
            end_date=self.end_date and self.end_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
            team_id=self.team_id
        )


class User(APIObject):
    def __init__(self, id, username, team_id):
        self.id = id
        self.username = username
        self.team_id = team_id

    @classmethod
    def from_dict(cls, data):
        if data:
            return cls(
                id=data['id'],
                username=data['username'],
                team_id=data['team_id']
            )

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            team_id=self.team_id
        )


class UserSurvey(APIObject):
    def __init__(self, id, user_id, survey_id, result):
        self.id = id
        self.user_id = user_id
        self.survey_id = survey_id
        self.result = result

    @classmethod
    def from_dict(cls, data):
        if data:
            return cls(
                id=data['id'],
                user_id=data['user_id'],
                survey_id=data['survey_id'],
                result=data['result']
            )

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            survey_id=self.survey_id,
            result=self.result
        )


class AddUserPayload(APIObject):
    def __init__(self, user_id):
        self.user_id = user_id

    @classmethod
    def from_dict(cls, data):
        if data:
            return cls(
                user_id=data['user_id']
            )

    def to_dict(self):
        return dict(
            user_id=self.user_id
        )


class VoteSurveyPayload(APIObject):
    def __init__(self, user_id, result):
        self.user_id = user_id
        self.result = result

    @classmethod
    def from_dict(cls, data):
        if data:
            return cls(
                user_id=data['user_id'],
                result=data['result']
            )

    def to_dict(self):
        return dict(
            user_id=self.user_id,
            result=self.result
        )
