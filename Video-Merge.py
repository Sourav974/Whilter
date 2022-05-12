from moviepy.editor import *

# Array of Dictionary of video details

attri = [
    {
        'name':'/Users/sourav/Downloads/Bhool Bhulaiya 1.mp4',
        'start_time':10,
        'end_time':40
    },
    
    {'name': '/Users/sourav/Downloads/Bhool Bhulaiyaa 2.mp4',
     'start_time': 50,
     'end_time': 100
    }
    
]


# Custom Exception Handling

class VideoError(Exception):
    def __init__(self, attri):
        self.attri = attri

    def checkVideo(self, attri):
        try:
            for i in range(len(attri)):
                for j in range(i + 1, len(attri)):

                    if attri[i]['start_time'] >= 0 and attri[i]['start_time'] < attri[i]['end_time']:
                        vid1 = VideoFileClip(attri[i]['name']).subclip(attri[i]['start_time'], attri[i]['end_time'])
                    else:
                        return ('start time should not negative or start time should always less than end time')

                    if attri[j]['start_time'] > attri[i]['end_time'] and attri[j]['start_time'] < attri[j]['end_time']:
                        vid2 = VideoFileClip(attri[j]['name']).subclip(attri[j]['start_time'], attri[j]['end_time'])

                    else:
                        return (
                            'start time should greater than first video or start time should always less than end time')

            return vid1, vid2


        except VideoError as ve:
            print("Please enter correct input")




# Object of VideoError Class
v = VideoError(attri)


# Merge Video Function
def merge(attri):
    videos = v.checkVideo(attri)
    final_clip = CompositeVideoClip(videos.checkVideo(attri))
    final_clip.write_videofile("/Users/sourav/Downloads/my_concatenation3.mp4", fps=30)

merge(attri)









# Implementation Of HashMap

# class MapNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# class Map:
#
#     def __init__(self):
#         self.bucketSize = 5
#         self.buckets = [None for i in range(self.bucketSize)]
#         self.count = 0
#
#     def size(self):
#         return self.count
#
#     def getBucketIndex(self, hc):
#         return (abs(hc) % (self.bucketSize))
#
#     def getValue(self, key):
#         hc = hash(key)
#         index = self.getBucketIndex(hc)
#         head = self.buckets[index]
#
#         while head is not None:
#             if head.key == key:
#                 return head.value
#
#             head = head.next
#
#         return None
#
#     def remove(self, key):
#         hc = hash(key)
#         index = self.getBucketIndex(hc)
#         head = self.buckets[index]
#         prev = None
#
#         while head is not None:
#             if head.key == key:
#                 if prev is None:
#                     self.buckets[index] = head.next
#                 else:
#                     prev.next = head.next
#                 self.count -= 1
#
#                 return head.value
#             prev = head
#             head = head.next
#
#         return None
#
#     def rehash(self):
#         temp = self.buckets
#         self.buckets = [None for i in range(2 * self.bucketSize)]
#         self.bucketSize = 2 * self.bucketSize
#         self.count = 0
#
#         for head in temp:
#             while head is not None:
#                 self.insert(head.key, head.value)
#                 head = head.next
#
#     def loadFactor(self):
#         return self.count / self.bucketSize
#
#     def insert(self, key, value):
#         hc = hash(key)
#         index = self.getBucketIndex(hc)
#         head = self.buckets[index]
#
#         while head is not None:
#             if head.key == key:
#                 head.value = value
#                 return
#             head = head.next
#
#         head = self.buckets[index]
#
#         newNode = MapNode(key, value)
#         newNode.next = head
#         self.buckets[index] = newNode
#         self.count += 1
#
#         loadFactor = self.count / self.bucketSize
#
#         if loadFactor >= 0.7:
#             self.rehash()
#
#
# m = Map()
# # m.insert('sourav', 13)
# # print(m.getValue('sourav'))
# # print(m.size())
#
# for i in range(10):
#     m.insert('abc' + str(i), i + 1)
#     print(m.loadFactor())
#
# # for i in range(10):
# #     print('abc'+str(i)+':', m.remove('abc'+str(i)))
#
