using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class button_menu : MonoBehaviour
{
    //i'm a designer with no coding experience, and this is an incomplete commit, i'm sorry if my code is atrocious ._.
    public void GoToproject_01()
    {
       
        SceneManager.LoadScene("project_01");
    }

    public void GoToproject_02()
    {
        SceneManager.LoadScene("project_02");
    }

  
}

