using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
public class FireController : MonoBehaviour
{
    int firePower = 2;
    int fireCount = 0;
    public bool blocked = false;
    public int fireDirection = 0;
    GameObject FireVertical;
    GameObject FireHorizontal;

    // Start is called before the first frame update
    void Start()
    {
        if(GameObject.FindGameObjectsWithTag("Player").Length != 0)
        {
            firePower = GameObject.FindGameObjectsWithTag("Player")[0].GetComponent<PlayerController>().bombPower;
        }
        FireVertical = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/FireVertical.prefab", typeof(GameObject));
        FireHorizontal = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/FireHorizontal.prefab", typeof(GameObject));
        GetComponent<Animator>().SetInteger("direction", fireDirection);
    }
    void Update()
    {
    }
    public void StartFire()
    {
        StartCoroutine(MakeFire(Vector2.down, fireCount));
        StartCoroutine(MakeFire(Vector2.right, fireCount));
        StartCoroutine(MakeFire(Vector2.up, fireCount));
        StartCoroutine(MakeFire(Vector2.left, fireCount));
        StartCoroutine(DestroyFire(fireCount));
    }
    public void FireMake(Vector2 direction, int count)
    {
        StartCoroutine(MakeFire(direction, count));
        StartCoroutine(DestroyFire(count));
    }
    public IEnumerator MakeFire(Vector2 direction, int count)
    {
        yield return new WaitForSeconds(0.05f);
        if(count != firePower && !blocked)
        {
            count++;
            RaycastHit2D hit = Physics2D.Raycast(transform.position + (Vector3)direction*0.075f, direction, 0.08f);
            if (hit.collider != null)
            {
                if (hit.collider.gameObject.tag == "Block")
                {
                    GameObject obj;
                    if (direction == Vector2.left || direction == Vector2.right)
                    {
                        obj = (GameObject)Instantiate(FireHorizontal);
                        obj.transform.position = transform.position + 0.17f * (Vector3)direction;
                        obj.GetComponent<FireController>().fireDirection = 1;
                        if (direction == Vector2.left)
                        {
                            obj.GetComponent<SpriteRenderer>().flipX = true;
                        }
                    }
                    else
                    {
                        obj = (GameObject)Instantiate(FireVertical);
                        obj.transform.position = transform.position + 0.16f * (Vector3)direction;
                        obj.GetComponent<FireController>().fireDirection = -1;
                        if(direction == Vector2.down)
                        {
                            obj.GetComponent<SpriteRenderer>().flipY = true;
                        }
                    }
                    obj.GetComponent<FireController>().blocked = true;
                    obj.GetComponent<FireController>().FireMake(direction, count);
                    Destroy(hit.collider.gameObject);
                }else if(hit.collider.gameObject.tag == "Bomb")
                {
                    hit.collider.gameObject.GetComponent<BombController>().Explosion();
                }else if(hit.collider.gameObject.tag == "Player")
                {
                    GameObject obj;
                    if (direction == Vector2.left || direction == Vector2.right)
                    {
                        obj = (GameObject)Instantiate(FireHorizontal);
                        obj.transform.position = transform.position + 0.17f * (Vector3)direction;
                    }
                    else
                    {
                        obj = (GameObject)Instantiate(FireVertical);
                        obj.transform.position = transform.position + 0.16f * (Vector3)direction;
                    }
                    obj.GetComponent<FireController>().FireMake(direction, count);
                }
            }
            else
            {
                GameObject obj;
                if(direction == Vector2.left || direction == Vector2.right)
                {
                    obj = (GameObject)Instantiate(FireHorizontal);
                    obj.transform.position = transform.position + 0.17f * (Vector3)direction;
                }
                else
                {
                    obj = (GameObject)Instantiate(FireVertical);
                    obj.transform.position = transform.position + 0.16f * (Vector3)direction;
                }
                obj.GetComponent<FireController>().FireMake(direction, count);
            }
        }
    }
    public IEnumerator DestroyFire(int count)
    {
        yield return new WaitForSeconds((11-count)*0.05f);
        Destroy(this.gameObject);
    }
}
