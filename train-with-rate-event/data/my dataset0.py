import predictionio

client = predictionio.EventClient(
  access_key="OnbeZSGcjdQQnwC6DL1cV6vmcpkZqIQgVzloN9p0KZV9XHDa5dKi6vrkoYvcevJ8",
  url="http://localhost:7070",
  threads=5,
  qsize=500
)

# Create a new user

user_ids = ["u%s" % i for i in range(0, 4)]
for user_id in user_ids:
    print "Set user", user_id
    client.create_event(
        event="$set",
        entity_type="user",
        entity_id=user_id
    )


# Create a new item
item_ids = ["i%s" % i for i in range(0, 6)]
for item_id in item_ids:
    print "Set item", item_id
    client.create_event(
        event="$set",
        entity_type="item",
        entity_id=item_id
    )

# def a new rating

def rating(user, item, rate):
    client.create_event(
	event="rate",
	entity_type="user",
	entity_id=user,
	target_entity_type="item",
	target_entity_id=item,
	properties={"rating" : float(rate)}
	)
print "def"
# create a new rating


rating("u0", "i0", 4)
rating("u0", "i1", 4)
rating("u0", "i2", 4)
rating("u0", "i3", 2)
rating("u0", "i4", 2)
rating("u0", "i5", 2)

rating("u1", "i0", 4)
rating("u1", "i1", 4)
rating("u1", "i2", 4)
rating("u1", "i3", 2)
rating("u1", "i4", 2)
rating("u1", "i5", 2)

rating("u2", "i0", 2)
rating("u2", "i1", 2)
rating("u2", "i2", 2)
rating("u2", "i3", 4)
rating("u2", "i4", 4)
rating("u2", "i5", 4)

rating("u3", "i0", 2)
rating("u3", "i1", 2)
rating("u3", "i2", 2)
rating("u3", "i3", 4)
rating("u3", "i4", 4)
rating("u3", "i5", 4)

rating("u4", "i1", 4)
rating("u4", "i2", 4)
rating("u4", "i3", 2)
rating("u4", "i4", 2)

print "rating"
