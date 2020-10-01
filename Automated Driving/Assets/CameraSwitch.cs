using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraSwitch : MonoBehaviour
{

    public GameObject Main_camera;
    public GameObject FP_camera;
    public GameObject L_Headlight_camera;
    public GameObject R_Headlight_camera;
    public GameObject R_Mirror;
    public GameObject L_Mirror;
    public GameObject DEFAULT_FP;


    // Use this for initialization
    void Start()
    {

        //Camera Position Set
        cameraPositionChange(PlayerPrefs.GetInt("CameraPosition"));
    }

    // Update is called once per frame
    void Update()
    {
        //Change Camera Keyboard
        switchCamera();
    }

    //UI JoyStick Method
    public void cameraPositonM()
    {
        cameraChangeCounter();
    }

    //Change Camera Keyboard
    void switchCamera()
    {
        if (Input.GetKeyDown(KeyCode.V))
        {
            cameraChangeCounter();
        }
    }

    //Camera Counter
    void cameraChangeCounter()
    {
        int cameraPositionCounter = PlayerPrefs.GetInt("CameraPosition");
        cameraPositionCounter++;
        cameraPositionChange(cameraPositionCounter);
    }

    //Camera change Logic
    void cameraPositionChange(int camPosition)
    {
        if (camPosition > 6)
        {
            camPosition = 0;
        }

        //Set camera position database
        PlayerPrefs.SetInt("CameraPosition", camPosition);

        //Set camera position 1
        if (camPosition == 0)
        {
            Main_camera.SetActive(true);
            FP_camera.SetActive(false);
            L_Headlight_camera.SetActive(false);
            R_Headlight_camera.SetActive(false);
            L_Mirror.SetActive(false);
            R_Mirror.SetActive(false);
            DEFAULT_FP.SetActive(false);
        }

        //Set camera position 2
        if (camPosition == 1)
        {
            Main_camera.SetActive(false);
            FP_camera.SetActive(true);
            L_Headlight_camera.SetActive(false);
            R_Headlight_camera.SetActive(false);
            L_Mirror.SetActive(false);
            R_Mirror.SetActive(false);
            DEFAULT_FP.SetActive(false);
        }

        //Set camera position 3
        if (camPosition == 2)
        {
            Main_camera.SetActive(false);
            FP_camera.SetActive(false);
            L_Headlight_camera.SetActive(true);
            R_Headlight_camera.SetActive(false);
            L_Mirror.SetActive(false);
            R_Mirror.SetActive(false);
            DEFAULT_FP.SetActive(false);
        }

        //Set camera position 4
        if (camPosition == 3)
        {
            Main_camera.SetActive(false);
            FP_camera.SetActive(false);
            L_Headlight_camera.SetActive(false);
            R_Headlight_camera.SetActive(true);
            L_Mirror.SetActive(false);
            R_Mirror.SetActive(false);
            DEFAULT_FP.SetActive(false);

        }


        if (camPosition == 4)
        {
            Main_camera.SetActive(false);
            FP_camera.SetActive(false);
            L_Headlight_camera.SetActive(false);
            R_Headlight_camera.SetActive(false);
            L_Mirror.SetActive(true);
            R_Mirror.SetActive(false);
            DEFAULT_FP.SetActive(false);
        }

        if (camPosition == 5)
        {
            Main_camera.SetActive(false);
            FP_camera.SetActive(false);
            L_Headlight_camera.SetActive(false);
            R_Headlight_camera.SetActive(false);
            L_Mirror.SetActive(false);
            R_Mirror.SetActive(true);
            DEFAULT_FP.SetActive(false);
        }

        if (camPosition == 6)
        {
            Main_camera.SetActive(false);
            FP_camera.SetActive(false);
            L_Headlight_camera.SetActive(false);
            R_Headlight_camera.SetActive(false);
            L_Mirror.SetActive(false);
            R_Mirror.SetActive(false);
            DEFAULT_FP.SetActive(true);
        }

    }
}