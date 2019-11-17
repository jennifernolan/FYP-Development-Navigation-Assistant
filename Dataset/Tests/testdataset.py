import pandas as pd
import os
import sys
import random

categories = ['Container', 'Football', 'Ambulance', 'Ladder', 'Sink', 'Toy', 'Organ(MusicalInstrument)', 'Parkingmeter', 'Trafficlight', 'Doll', 'Washingmachine','Cart', 'Ball', 'Backpack', 'Bicycle', 'Homeappliance', 'Boat', 'Surfboard', 'Boot', 'Bus', 'Boy', 'Bicyclewheel', 'Barge', 'Tower', 'Person', 'Tent', 'Billboard', 'Stairs', 'Trafficsign', 'Chair', 'Poster', 'Firehydrant', 'Landvehicle', 'Suitcase', 'Bidet', 'Snowmobile', 'Clock', 'Medicalequipment', 'Cattle', 'Desk', 'Bronzesculpture', 'Officebuilding', 'Fountain', 'Computermonitor', 'Box', 'Christmastree', 'Hikingequipment', 'Studiocouch', 'Drum', 'Oven', 'Whiteboard', 'Door', 'Shower', 'Stretcher', 'Stopsign', 'Vase', 'Wardrobe', 'Flyingdisc', 'Gasstove', 'Mechanicalfan', 'Nightstand', 'Barrel', 'Treadmill', 'Windowblind', 'Golfcart', 'Streetlight', 'Doorhandle', 'Bathtub', 'Houseplant', 'Stationarybicycle', 'Ceilingfan', 'Curtain', 'Bed', 'Fireplace', 'Scale', 'Indoorrower', 'Bookcase', 'Refrigerator', 'Wood-burningstove', 'Punchingbag', 'Filingcabinet', 'Table', 'Humidifier', 'Porch', 'Billiardtable', 'Motorcycle', 'Musicalinstrument', 'Snowplow', 'Bathroomcabinet', 'Mirror', 'Musicalkeyboard', 'Scoreboard', 'Briefcase', 'Plasticbag', 'Chestofdrawers', 'Piano', 'Girl', 'Plant', 'Sportsequipment', 'Infantbed', 'Cupboard', 'Jacuzzi', 'Skateboard', 'Snowboard', 'Loveseat', 'Trainingbench', 'Coffeetable', 'Skyscraper', 'Television', 'Train', 'Handbag', 'Toilet', 'Wastecontainer', 'Swimmingpool', 'Handdryer', 'Palmtree', 'Furniture', 'Conveniencestore', 'Bench', 'Window', 'Closet', 'Castle', 'Lamp', 'Flowerpot', 'Drawer', 'Stool', 'Shelf', 'Van', 'Wallclock', 'Kitchendiningroomtable', 'Dogbed', 'Kitchenappliance', 'Luggageandbags', 'Umbrella', 'Dishwasher', 'Taxi', 'Wheelchair', 'Rugbyball']

base_path = 'OIDv4_ToolKit/OID/Dataset/'

test_path = os.path.join(base_path, 'test')

annotations_bbox = pd.read_csv('Original Datasets/test-annotations-bbox.csv')

kwargs = {'header': None, 'names': ['LabelID', 'ClassName']}
class_descriptions = pd.read_csv('Original Datasets/class-descriptions-boxable.csv', **kwargs)

test_df = pd.DataFrame(columns = ['FileName', 'OriginalURL', 'XMin', 'XMax', 'YMin', 'YMax', 'ClassName'])

all_imgs = []


for i in range(len(categories)):
    all_imgs.append(os.listdir(os.path.join(test_path, categories[i])))

every_img = []

for i in range(len(all_imgs)):
    for j in range(len(all_imgs[i])):
        every_img.append(all_imgs[i][j])

label_names = []

for i in range(len(categories)):
    classes = class_descriptions[class_descriptions['ClassName'] == categories[i]]
    label_names.append(classes['LabelID'].values[0])

urlbase = 'https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/test/'
  
for i in range(len(every_img)):
    sys.stdout.write('Parse all_imgs ' + str(i) + '; Number of boxes: ' + str(len(test_df)) + '\r')
    sys.stdout.flush()
    img_name = every_img[i]
    img_id = img_name[0:16]
    tmp_df = annotations_bbox[annotations_bbox['ImageID'] == img_id]
    url = urlbase + img_name
    for index, row in tmp_df.iterrows():
        labelName = row['LabelName']
        for i in range(len(label_names)):
            if labelName == label_names[i]:
                test_df = test_df.append({'FileName': img_name,
                                            'OriginalURL': url,
                                            'XMin': row['XMin'],
                                            'XMax': row['XMax'],
                                            'YMin': row['YMin'],
                                            'YMax': row['YMax'],
                                            'ClassName': categories[i]},
                                            ignore_index = True)
                                            
                                            

<<<<<<< HEAD
test_df.to_csv('test.csv', index = False)
=======
test_df.to_csv('test.csv', index = False)
>>>>>>> f571d33716aedbfbd5c80e786abf096686198714
