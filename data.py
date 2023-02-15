import csv
import os


def create_file():

    if not os.path.isfile('cache/data.csv'):
        with open('cache/data.csv', 'w', newline='') as file:
            names = ['owner_id', 'post_id', 'p_date', 'p_text', 'p_att', 'comm_id', 'c_text', 'c_att', 'c_like']  # заголовки в csv файл

            file_writer = csv.DictWriter(file, delimiter=";", fieldnames=names)
            file_writer.writeheader()

    else:
        pass


def write_file(owner_id, post_id, p_date, comm_id, p_text='', p_att='', c_text='', c_att='', c_like=''):

    with open('cache/data.csv', 'a', newline='') as file:
        names = ['owner_id', 'post_id', 'p_date', 'p_text', 'p_att', 'comm_id', 'c_text', 'c_att', 'c_like']
        file_writer = csv.DictWriter(file, delimiter=";", fieldnames=names)

        file_writer.writerow({"owner_id": owner_id, "post_id": post_id, "p_date": p_date, "p_text": p_text, "p_att": p_att,
                              "comm_id": comm_id, "c_text": c_text, "c_att": c_att, "c_like": c_like})


if __name__ == '__main__':
    pass
