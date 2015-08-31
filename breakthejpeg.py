from random import randrange
import oauth2 as oauth
import sys


def breakthejpeg(file_path, out_file_path = None):
    repetitions = randrange(1, 15)
    max_chunk_size = 10000
    in_file = open(file_path, mode='rb')
    out_file = open(out_file_path, mode='wb')

    chunk = " "
    while len(chunk) > 0:
        chunk = in_file.read(max_chunk_size)
        if repetitions > 0:
            if randrange(0, 2) > 0:
                repetitions -= 1
                chunk = chunk[-5]
                print "chunky!"
        out_file.write(chunk)

def upload_picture():
    # http://stackoverflow.com/questions/27801189/how-to-update-profile-image-to-twitter-using-rest-api
    # https://github.com/joestump/python-oauth2
    pass

if __name__ == '__main__':
    breakthejpeg(sys.argv[1], sys.argv[2])
    upload_picture()
