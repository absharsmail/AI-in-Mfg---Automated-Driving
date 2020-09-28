using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class player : MonoBehaviour
{
    // Start is called before the first frame update
    public Rigidbody rb;
    public float force = 500f;
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey("w"))
        {
            rb.AddForce(force * Time.deltaTime, 0, 0);
        }
        if (Input.GetKey("s"))
        {
            rb.AddForce(-force * Time.deltaTime, 0, 0);
        }
        if (Input.GetKey("a"))
        {
            rb.AddForce(0, 0, force * Time.deltaTime);
        }
        if (Input.GetKey("d"))
        {
            rb.AddForce(0, 0, -force * Time.deltaTime);
        }
    }
}
