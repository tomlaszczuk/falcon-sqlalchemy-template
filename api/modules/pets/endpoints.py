import falcon

import ujson as json

from api.models import Pet


class PetCollection:

    def on_get(self, req, resp):
        items = self.session.query(Pet).all()
        data = [
            {'id': item.id, 'name': item.name} for item in items
        ]
        resp.body = json.dumps(data)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        body = req.stream.read()
        if body:
            print(body)
            data = json.loads(body)
            name = data.get('name')
            if name:
                pet = Pet(name=name)
                self.session.begin()
                self.session.add(pet)
                self.session.commit()
                resp.status = falcon.HTTP_201
                resp.body = json.dumps({'name': name, 'id': pet.id})
                resp.location = '/pets/%d' % pet.id
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({'name': 'nic'})
