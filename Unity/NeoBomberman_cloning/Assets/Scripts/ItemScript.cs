using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ItemScript : MonoBehaviour
{
    public int itemNumber = 0;
    // Start is called before the first frame update
    void Start()
    {

    }
    void OnTriggerEnter2D(Collider2D other)
    {
        if(other.gameObject.tag == "Player")
        {
            switch (itemNumber)
            {
                case 1:
                    other.gameObject.GetComponent<PlayerController>().bombCount += 1;
                    break;
                case 2:
                    other.gameObject.GetComponent<PlayerController>().SetSpeed();
                    break;
                default:
                    break;
            }
            Destroy(this.gameObject);
        }
        
    }
}
