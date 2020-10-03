using System.Collections;
using System.Collections.Generic;
using System.Threading;
using UnityEngine;

public class CameraControl : MonoBehaviour
{
    public GameObject Player;
    public float speed;
    public Vector3 Offset;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void FixedUpdate()
    {
        follow();
    }

    void follow()
    {
        gameObject.transform.position = Vector3.Lerp(gameObject.transform.position, Player.transform.position, Time.deltaTime * speed) + Offset;
        gameObject.transform.LookAt(Player.gameObject.transform.position);
    }
}
