class Global(object):
    room_list = []
    room_id = 0

class Room(Global):
    def __init__(self, username):
            self.room_id = Global.room_id + 1
            Global.room_id = Global.room_id + 1
            self.room_name = username.lower()       # room_name is same as first or last remaining username
            try: self.users
            except: self.users = []

            self.users.append(username.lower())

            Global.room_list.append(self)

    def join(self, username):
        self.users.append(username)

    def leave(self, username):
        try: 
            self.users.remove(username)
            if len(self.users) < 1:
                del self
            return True
        except:
            return False
        
    @property
    def Info(self):
        return '{} {} - {}'.format(self.room_id, self.room_name, self.users)

    @staticmethod
    def getSelf():
        return  Global.room_list

    @staticmethod
    def IsExists(room_name):
        if room_name.lower() in [room.room_name for room in Global.room_list]:
            return True
        return False

    @staticmethod
    def find(username):
        for room in Global.room_list:
            if username.lower() == room.room_name:
                return room
        return False
