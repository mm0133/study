using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

public class PlayerController : MonoBehaviour
{
    public int bombPower = 2;
    public int bombCount = 1;
    public int speedLevel = 0;
    float moveSpeed = 0.5f;
    bool kickAbility;
    bool throwAbility;
    public Vector2 moveDirection;
    Animator animator;
    Rigidbody2D rb2D;
    GameObject BombObj;
    GameObject[] Lattice;


// Start is called before the first frame update
    void Start()
    {
        BombObj = (GameObject)AssetDatabase.LoadAssetAtPath("Assets/Prefabs/Bomb.prefab", typeof(GameObject));
        animator = GetComponent<Animator>();
        rb2D = GetComponent<Rigidbody2D>();
    }
    // Update is called once per frame
    void Update()
    {
        movePlayer();
        SetBomb();
    }


    void movePlayer()
    {
        if (Input.GetKey(KeyCode.DownArrow))
        {
            PathFinding(Vector2.down);
            animator.SetInteger("Direction", 0);
        }else if (Input.GetKey(KeyCode.RightArrow))
        {
            PathFinding(Vector2.right);
            animator.SetInteger("Direction", 1);
        }
        else if (Input.GetKey(KeyCode.UpArrow))
        {
            PathFinding(Vector2.up);
            animator.SetInteger("Direction", 2);
        }
        else if (Input.GetKey(KeyCode.LeftArrow))
        {
            PathFinding(Vector2.left);
            animator.SetInteger("Direction", 3);
        }
        else
        {
            moveDirection = Vector2.zero;
        }
        animator.SetBool("IsMoving", moveDirection != Vector2.zero);
        rb2D.velocity = moveSpeed * moveDirection;
    }
    void PathFinding(Vector2 direction)
    {
        var layerMask = (1 << 8) | (1 << 11);
        layerMask = ~layerMask;
        RaycastHit2D hit = Physics2D.BoxCast(transform.position + new Vector3(0, 0.08f), new Vector2(0.13f, 0.12f), 0, direction, 0.05f, layerMask);
        if(hit.collider != null)
        {
            if (direction == Vector2.up || direction == Vector2.down)
            {
                RaycastHit2D hit_Right = Physics2D.Raycast(transform.position + new Vector3(0, 0.08f) + new Vector3(0.08f, 0), direction, 0.16f, layerMask);
                RaycastHit2D hit_Left = Physics2D.Raycast(transform.position + new Vector3(0, 0.08f) - new Vector3(0.08f, 0), direction, 0.16f, layerMask);
                if (hit_Right.collider != null && hit_Left.collider != null)
                {
                    moveDirection = direction;
                }
                else if (hit_Right.collider == null)
                {
                    moveDirection = Vector2.right;
                }
                else if (hit_Left.collider == null)
                {
                    moveDirection = Vector2.left;
                }
            }
            else
            {
                RaycastHit2D hit_Top = Physics2D.Raycast(transform.position + new Vector3(0, 0.08f) + new Vector3(0, 0.085f), direction, 0.16f, layerMask);
                RaycastHit2D hit_Bottom = Physics2D.Raycast(transform.position + new Vector3(0, 0.08f) - new Vector3(0, 0.085f), direction, 0.16f, layerMask);
                if (hit_Top.collider != null && hit_Bottom.collider != null)
                {
                    moveDirection = direction;
                }
                else if (hit_Top.collider == null)
                {
                    moveDirection = Vector2.up;
                }
                else if (hit_Bottom.collider == null)
                {
                    moveDirection = Vector2.down;
                }
            }
        }
        else
        {
            moveDirection = direction;
        }
    }
    void SetBomb()
    {
        if (Input.GetKeyDown(KeyCode.Q) && GameObject.FindGameObjectsWithTag("Bomb").Length < bombCount)
        {
            GameObject obj = (GameObject)Instantiate(BombObj);
            FindtLatticePoint(obj);
        }
    }
    void FindtLatticePoint(GameObject obj)
    {
        Lattice = GameObject.FindGameObjectsWithTag("Tile");
        float distance = 100.0f;
        int index = 0;
        for(int i = 0; i < Lattice.Length; i++)
        {
            if(distance > (Lattice[i].transform.position - transform.position).magnitude)
            {
                distance = (Lattice[i].transform.position - transform.position).magnitude;
                index = i;
            }
        }
        obj.transform.position = Lattice[index].transform.position;
    }
    public void SetSpeed()
    {
        speedLevel += 1;
        moveSpeed = 0.5f + 0.1f * speedLevel;
    }

}
