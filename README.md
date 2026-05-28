EmotionDetectionEcommerce
Final Project: AI-Based Web Application Development and Deployment
Estimated Time: 1 hour 45 minutes
Scenario
You have been hired as a software engineer by an e-commerce company to create an AI-based web app that performs analytics on customer feedback for their signature products. To accomplish this requirement, you will create an Emotion Detection system that processes feedback provided by the customer in text format and deciphers the associated emotion expressed.

Introduction
In this final project, you will be assessed on the knowledge gained on all aspects of app creation and its web deployment throughout this course. You will be required to save screenshots of your results from time to time, with specific nomenclature. These screenshots will have to be uploaded in the peer-graded assignment that follows.

In this project, we use the embeddable Watson AI libraries to create an emotion detection application.

Emotion detection extends the concept of sentiment analysis by extracting finer emotions, like joy, sadness, anger, and more, rather than just polarity. Businesses widely use such systems for AI-based recommendation systems, automated chatbots, and more.

Project Guidelines
For the completion of this project, you'll have to complete the following 8 tasks, based on the knowledge you have gained through the course.

Note: This platform is not persistent. It is recommended that you keep a copy of your code on your local machines and save changes regularly. In case you revisit the lab, you will need to recreate the files using the saved copies from your machines.

Tasks and Objectives
Task 1: Fork and Clone the Project Repository
Fork the repository from GitHub: Project Repository
Ensure your forked repository is Public.
Open a new Terminal and create the final_project directory using:
mkdir final_project
Clone the forked repository:
git clone <your_forked_repository_url> final_project
Navigate to the final_project directory:
cd final_project
Take a screenshot of your folder structure and save it as 1_folder_structure.png.
Task 2: Create an Emotion Detection Application using Watson NLP Library
Create a file named emotion_detection.py in the final_project folder.
Implement the emotion_detector function that sends a POST request to the Watson NLP Emotion Predict API.
Test the function using the Python shell:
python3.11
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology.")
Take a screenshot of your terminal output and save it as 2b_application_creation.png.
Task 3: Format the Output of the Application
Convert the API response into a dictionary using the json library.
Extract emotions: anger, disgust, fear, joy, sadness.
Determine the dominant emotion.
Modify emotion_detector to return:
{
    "anger": anger_score,
    "disgust": disgust_score,
    "fear": fear_score,
    "joy": joy_score,
    "sadness": sadness_score,
    "dominant_emotion": "<name of the dominant emotion>"
}
Take a screenshot and save it as 3a_output_formatting.png.
Task 4: Package the Application
Create a package named EmotionDetection.
Take a screenshot of the __init__.py file and folder structure, saving it as 4a_packaging.png.
Test the package:
python3.11
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I hate working long hours.")
Take a screenshot and save it as 4b_packaging_test.png.
Task 5: Run Unit Tests on Your Application
Create test_emotion_detection.py.
Write tests for:
Statement	Dominant Emotion
I am glad this happened	joy
I am really mad about this	anger
I feel disgusted just hearing about this	disgust
I am so sad about this	sadness
I am really afraid that this will happen	fear
Execute the test file:
python3.11 test_emotion_detection.py
Take a screenshot of the terminal output and save it as 5b_unit_testing_result.png.
Task 6: Web Deployment of the Application using Flask
Create server.py in final_project.
Ensure the Flask route is /emotionDetector.
Deploy the app on localhost:5000.
Take a screenshot of server.py as 6a_server.png.
Test with: "I think I am having fun" and take a screenshot as 6b_deployment_test.png.
Task 7: Incorporate Error Handling
Modify emotion_detector to handle blank inputs (return None values for all keys).
Modify server.py to return "Invalid text! Please try again!" for blank entries.
Test error handling and save screenshots:
7a_error_handling_function.png
7b_error_handling_server.png
7c_error_handling_interface.png
Task 8: Run Static Code Analysis
Run Pylint on emotion_detection.py:
pylint emotion_detection.py
Take a screenshot of the output and save it as 8a_static_analysis.png.
Optional: Push Your Code to GitHub
At any point, push your code to your GitHub repository:

cd final_project
git add .
git commit -m "Final project submission"
git push origin main
Conclusion
By completing this project, you will gain hands-on experience in AI-based web app development, API integration, error handling, unit testing, packaging, and deployment using Flask.
