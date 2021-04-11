using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

public class BlockScript : MonoBehaviour
{
    public int itemNumber;
    GameObject ItemObj;
    // Start is called before the first frame update
    void Start()
    {
        ItemObj = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Item.prefab", typeof(GameObject));
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    void OnDestroy()
    {
        if(itemNumber != 0)
        {
            GameObject obj = (GameObject)Instantiate(ItemObj);
            obj.transform.position = transform.position;
            obj.GetComponent<Animator>().SetInteger("ItemNumber", itemNumber);
            obj.GetComponent<ItemScript>().itemNumber = itemNumber;
        }
    }
}
