import requests

payload = {
    'email': 'rajdeeprusted',
    'pass': 'notmypassword'
}

page = requests.get('https://www.facebook.com/rajdeeprusted/friends')
tree = html.fromstring(page.content)
friends = tree.xpath('//a/span/text()')

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://www.facebook.com', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    tree = html.fromstring(p.content)
    friends = tree.xpath('//imaage/href/text()')
    print("Facebook" in p.text)
    # An authorised request.
    #r = s.get('A protected web page url')
    #print r.text
        # etc...

