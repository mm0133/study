using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

public class BombController : MonoBehaviour
{
    
    GameObject FireObj;
    // Start is called before the first frame update
    void Start()
    {
        FireObj = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Fire.prefab", typeof(GameObject));
        StartCoroutine(Explode());
    }

    // Update is called once per frame
    void Update()
    {
        if((GameObject.FindGameObjectsWithTag("Player")[0].transform.position - transform.position).magnitude <= 0.16f)
        {
            gameObject.layer = 8;
        }
        else
        {
            gameObject.layer = 9;
        }
    }
    IEnumerator Explode()
    {
        yield return new WaitForSeconds(2.5f);
        Explosion();
    }
    public void Explosion()
    {
        GameObject obj = (GameObject)Instantiate(FireObj);
        obj.transform.position = transform.position + (Vector3)(Vector2.up * 0.08f);
        obj.GetComponent<FireController>().StartFire();
        Destroy(this.gameObject);
    }
}
