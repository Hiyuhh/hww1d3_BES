from flask import Flask, request, jsonify

app = Flask(__name__)

videos = [
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]


def vid_search(lst, title):
    lst.sort(key=lambda x: x['title'])
    
    low = 0
    high = len(lst) - 1
    num_checks = 0
    while low <= high:
        mid = (low + high) // 2
        mid_title = lst[mid]['title']
        num_checks += 1
        if title == mid_title:
            return lst[mid]
        elif title > mid_title:
            low = mid + 1
        else:
            high = mid - 1
    return None

print(vid_search(videos,"The Art of Coding"))



@app.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Search is required'}), 400
    
    matching_videos = vid_search(videos, query)
    
    if matching_videos:
        return jsonify(matching_videos)
    else:
        return jsonify({'message': 'No videos found'}), 404


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        l = r = m = 0

        while l < len(left_half) and r < len(right_half):
            if left_half[l]["title"] < right_half[r]["title"]:
                lst[m] = left_half[l]
                l += 1
            else:
                lst[m] = right_half[r]
                r += 1
            m += 1

        while l < len(left_half):
            lst[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1
    return lst

print(merge_sort(videos))

@app.route('/sorted-vids', methods=['GET'])
def get_sorted_videos():
    sorted_vids = merge_sort(videos)
    return jsonify(sorted_vids)

if __name__ == '__main__':
    app.run(debug=True)

