using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System.Text;

public class HumanoidBoneListOutputforBlender : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
                // Humanoidアバターのボーンの対応を出力
        string objectName = this.gameObject.name;
        //任意のアセットパスに変更してください
        StreamWriter sw = new StreamWriter(@"Assets\D9speed\"+objectName+"_BoneList.txt",false);
        HumanDescription description = GetComponent<Animator>().avatar.humanDescription;
        sw.Write("{");
        for (int i = 0; i < description.human.Length; i++)
        {
            //JSON形式のテキストファイルで書き出します
            
            string human_NameBone_Name = "'"+description.human[i].humanName+"'" + ":" + "'"+description.human[i].boneName+"'"+",";
            //string indexAsString = i.ToString();
            //sw.Write( "'" + indexAsString + "'" + ":");
            sw.WriteLine(human_NameBone_Name);
            
        }
        sw.Write("}");
        sw.Close();
    }

    // Update is called once per frame
    void Update()
    {}
}
