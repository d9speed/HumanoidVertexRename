import bpy
from ast import literal_eval
import time
import pprint
import numpy as np

#頂点グループをリネームしたい"服の"オブジェクト選択
obj = bpy.context.active_object
obj_vg = obj.vertex_groups

#着せ替えたいアバターと服のヒューマノイド定義両方必要
with (open(r"U:\アセットいろいろ\00マッハ着せ替えツールVertexGroup_Ditionary\あまとううさぎ_LimeBoneList.txt", 'r', encoding="utf-8") as AvatarBoneList,
    open(r"U:\アセットいろいろ\00マッハ着せ替えツールVertexGroup_Ditionary\Masscat 2 (kisekae)_BoneList.txt", 'r', encoding="utf-8" )as TGClothHumanoidList):

    #評価済みテキスト(辞書型に変換したテキストファイル)を返す標準ライブラリを利用
    AvatarHumanoid = literal_eval(AvatarBoneList.read())
    TGHumanoid = literal_eval(TGClothHumanoidList.read())


# 服のボーンは、手だけなかったりするので辞書型でペアちゃんと作って
# 一致で処理したほうが確実

FullListedHumanoidBone = {
 'Hips': None,
 'LeftUpperLeg': None,
 'RightUpperLeg': None,
 'LeftLowerLeg': None,
 'RightLowerLeg': None,
 'LeftFoot': None,
 'RightFoot': None,
 'Spine': None,
 'Chest': None,
 'Neck': None,
 'Head': None,
 'LeftShoulder': None,
 'RightShoulder': None,
 'LeftUpperArm': None,
 'RightUpperArm': None,
 'LeftLowerArm': None,
 'RightLowerArm': None,
 'LeftHand': None,
 'RightHand': None,
 'LeftToes': None,
 'RightToes': None,
 'LeftEye': None,
 'RightEye': None,
 'Left Thumb Proximal': None,
 'Left Thumb Intermediate': None,
 'Left Thumb Distal': None,
 'Left Index Proximal': None,
 'Left Index Intermediate': None,
 'Left Index Distal': None,
 'Left Middle Proximal': None,
 'Left Middle Intermediate': None,
 'Left Middle Distal': None,
 'Left Ring Proximal': None,
 'Left Ring Intermediate': None,
 'Left Ring Distal': None,
 'Left Little Proximal': None,
 'Left Little Intermediate': None,
 'Left Little Distal': None,
 'Right Thumb Proximal': None,
 'Right Thumb Intermediate': None,
 'Right Thumb Distal': None,
 'Right Index Proximal': None,
 'Right Index Intermediate': None,
 'Right Index Distal': None,
 'Right Middle Proximal': None,
 'Right Middle Intermediate': None,
 'Right Middle Distal': None,
 'Right Ring Proximal': None,
 'Right Ring Intermediate': None,
 'Right Ring Distal': None,
 'Right Little Proximal': None,
 'Right Little Intermediate': None,
 'Right Little Distal': None
 }

#辞書のコピー
Avadict = dict(FullListedHumanoidBone.items())
Avadict.update(AvatarHumanoid)

ClothDict = dict(FullListedHumanoidBone.items())
ClothDict.update(TGHumanoid)

Unity_AvatarHumanoid_vg_index = list(AvatarHumanoid.values())
Unity_Cloth_Target_Bone_vg_index = list(TGHumanoid.values())

#位置初期化
obj_vg.active_index = 0

#集合演算
intersects = np.intersect1d(Unity_Cloth_Target_Bone_vg_index, list(obj_vg.keys()))
isin = np.isin(Unity_Cloth_Target_Bone_vg_index, list(obj_vg.keys()))
indices, = np.where(isin)
sortedMeshVG = sorted(intersects,key=Unity_Cloth_Target_Bone_vg_index.index)


#Unityヒューマノイドに準じて服(UnityHumanoid)→服(BlenderのVG)並べ替え
for index,i in enumerate(sortedMeshVG):
    if i in obj_vg.keys():
        obj_vg.active_index = obj_vg[i].index
        while index < obj_vg[i].index:
              bpy.ops.object.vertex_group_move(direction='UP')

HumnanoidBonekey =list(TGHumanoid.keys())
HumnanoidBonekey = [item for index,item in enumerate(HumnanoidBonekey) if index in indices]

#辞書作成
override_name_dictionary = dict(zip(HumnanoidBonekey,sortedMeshVG))
common_keys = set(AvatarHumanoid.keys()) & set(override_name_dictionary.keys())
comlist=list(common_keys)

#リネーム
for index,key in enumerate(common_keys):
    if key in AvatarHumanoid.keys():
            obj_vg[override_name_dictionary[key]].name = AvatarHumanoid[key]