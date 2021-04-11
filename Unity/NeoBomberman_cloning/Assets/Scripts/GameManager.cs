using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.IO;

public class GameManager : MonoBehaviour
{
    int stage = 0;
    static float unit_X = 0.17f;
    static float unit_Y = 0.16f;
    static int[,] stage_01 = new int[,]{
        {0,0,0,2,0,2,2,0,2,0,0,0,0 },
        {0,1,1,1,2,1,2,1,0,1,1,1,0 },
        {2,1,0,0,0,0,0,0,0,0,0,1,2 },
        {2,1,0,1,1,1,0,1,1,1,0,1,2 },
        {0,0,0,1,0,2,0,2,0,1,2,2,0 },
        {2,1,2,1,2,1,0,1,0,1,0,1,2 },
        {2,1,2,2,0,2,0,2,0,0,0,0,0 },
        {0,1,2,1,0,1,0,1,2,1,1,1,1 },
        {0,1,0,0,0,2,0,2,0,2,0,2,0 },
        {0,1,1,1,2,1,0,1,2,1,2,1,0 },
        {0,0,0,0,0,0,3,0,0,0,0,0,0 }
    };
    static int[][,] MapInfo = new int[][,] { stage_01 };
    static int[] item_01 = new int[] { 2, 1, 0, 0, 0, 0, 0, 0 }; //BombUp, SpeedUp, PowerUp, Kick, asdfasdf
    static int[] item_02 = new int[] { 0, 1, 1, 1, 0, 0, 0, 0 };
    static int[][] ItemInfo = new int[][] { item_01, item_02 };

    GameObject MapTile;
    GameObject BottomObj;
    GameObject TopObj;
    GameObject ExitObj;
    GameObject PlayerObj;
    GameObject BlockObj;

    GameObject Collider_Top;
    GameObject Collider_Bottom;
    GameObject Collider_Right;
    GameObject Collider_Left;

    GameObject MapEdge;

    GameObject[] Colliders;
    GameObject[] MapObjects;
    // Start is called before the first frame update
    void Start()
    {
        MapTile = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/MapTile.prefab", typeof(GameObject));
        BottomObj = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/MapObject_Bottom.prefab", typeof(GameObject));
        TopObj = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/MapObject_Top.prefab", typeof(GameObject));
        ExitObj = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Exit.prefab", typeof(GameObject));
        BlockObj = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Block.prefab", typeof(GameObject));
        PlayerObj = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/player.prefab", typeof(GameObject));

        Collider_Top = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Collider/Collider_Top.prefab", typeof(GameObject));
        Collider_Bottom = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Collider/Collider_Bottom.prefab", typeof(GameObject));
        Collider_Right = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Collider/Collider_Right.prefab", typeof(GameObject));
        Collider_Left = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Collider/Collider_Left.prefab", typeof(GameObject));

        Colliders = new GameObject[] { Collider_Bottom, Collider_Right, Collider_Top, Collider_Left };
        MapObjects = new GameObject[] {MapTile, BottomObj, BlockObj, ExitObj, TopObj };

        MapEdge = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Collider/MapEdge.prefab", typeof(GameObject));

        
        MakeStage(stage);
        SetItems(stage);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    void MakeStage(int stageNum)
    {
        GameObject EmptyObj = new GameObject("Map");
        GameObject EmptyObj_2 = new GameObject("Colliders");
        for (int x = 0; x < 13; x++)
        {
            for(int y = 0; y < 11; y++)
            {
                GameObject obj = (GameObject)Instantiate(MapObjects[0]);
                obj.transform.position = new Vector2((x-6)*unit_X, (5-y)*unit_Y);
                obj.transform.parent = EmptyObj.transform;
                if(MapInfo[stageNum][y,x] != 0)
                {
                    GameObject obj_2 = (GameObject)Instantiate(MapObjects[MapInfo[stageNum][y,x]]);
                    obj_2.transform.position = new Vector2((x-6) * unit_X, (5-y) * unit_Y);
                    obj_2.transform.parent = EmptyObj.transform;
                    if(MapInfo[stageNum][y,x] == 1)
                    {
                        GameObject obj_3 = (GameObject)Instantiate(MapObjects[4]);
                        obj_3.transform.position = new Vector2((x - 6) * unit_X, (6 - y) * unit_Y);
                        obj_3.transform.parent = EmptyObj.transform;
                        if(x != 12)
                        {
                            if (MapInfo[stageNum][y, x + 1] != 1)
                            {
                                GameObject obj_4 = (GameObject)Instantiate(Collider_Right);
                                obj_4.transform.position = new Vector2((x - 6) * unit_X, (5 - y) * unit_Y);
                                obj_4.transform.parent = EmptyObj_2.transform;
                            }
                        }
                        if(x != 0)
                        {
                            if (MapInfo[stageNum][y, x - 1] != 1)
                            {
                                GameObject obj_4 = (GameObject)Instantiate(Collider_Left);
                                obj_4.transform.position = new Vector2((x - 6) * unit_X, (5 - y) * unit_Y);
                                obj_4.transform.parent = EmptyObj_2.transform;
                            }
                        }
                        if (y != 0)
                        {
                            if (MapInfo[stageNum][y-1, x] != 1)
                            {
                                GameObject obj_4 = (GameObject)Instantiate(Collider_Top);
                                obj_4.transform.position = new Vector2((x - 6) * unit_X, (5 - y) * unit_Y);
                                obj_4.transform.parent = EmptyObj_2.transform;
                            }
                        }
                        if (y != 10)
                        {
                            if (MapInfo[stageNum][y + 1, x] != 1)
                            {
                                GameObject obj_4 = (GameObject)Instantiate(Collider_Bottom);
                                obj_4.transform.position = new Vector2((x - 6) * unit_X, (5 - y) * unit_Y);
                                obj_4.transform.parent = EmptyObj_2.transform;
                            }
                        }
                    }else if(MapInfo[stageNum][y, x] == 2)
                    {

                    }
                }
            }
        }
        GameObject player = (GameObject)Instantiate(PlayerObj);
        MapEdge = (GameObject)Instantiate(MapEdge);
        player.transform.position = new Vector2(-6*unit_X, 5*unit_Y);
    }
    int[] MakeRandomNumbers(int size, int count)
    {
        int[] temp = new int[count];
        int itemSetting = 0;
        bool checkSameInt = false;
        while(itemSetting < count)
        {
            checkSameInt = false;
            int randInt = Random.Range(0, size); // Random.Range(0, n) 0 ~ n-1
            for(int i = 0; i < count; i++)
            {
                if(temp[i] == randInt)
                {
                    checkSameInt = true;
                }
            }
            if (!checkSameInt)
            {
                temp[itemSetting] = randInt;
                itemSetting += 1;
            }
        }
        return temp;
    }
    void SetItems(int stageNum)
    {
        int count = 0;
        for(int i = 0; i < ItemInfo[stageNum].Length; i++)
        {
            count += ItemInfo[stageNum][i];
        }
        int[] blockNumber = MakeRandomNumbers(GameObject.FindGameObjectsWithTag("Block").Length, count);
        for (int i = 0; i < ItemInfo[stageNum].Length; i++)
        {
            for(int j = 0; j < ItemInfo[stageNum][i]; j++)
            {
                if(count > 0)
                {
                    GameObject.FindGameObjectsWithTag("Block")[blockNumber[count - 1]].GetComponent<BlockScript>().itemNumber = i+1;
                    count -= 1;
                }
            }
        }
    }
}
