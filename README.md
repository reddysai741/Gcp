# From Day1 To Day 10 of Gcp Training

### Content What I have done in this training!



<img width="1337" height="449" alt="Screenshot 2025-12-23 111345" src="https://github.com/user-attachments/assets/283ce319-7a81-471a-bfa1-1032e133b2ed" />
<img width="840" height="72" alt="Screenshot 2025-12-23 102114" src="https://github.com/user-attachments/assets/7d67619d-4747-4140-b494-26365883f773" />
<img width="1134" height="424" alt="Screenshot 2025-12-23 101925" src="https://github.com/user-attachments/assets/66014979-252b-40fa-9dad-71aec5a685ea" />
<img width="869" height="77" alt="Screenshot 2025-12-23 101732" src="https://github.com/user-attachments/assets/6c6a9eba-39d3-4ca1-bf5a-4380d9ef9348" />
<img width="1138" height="498" alt="Screenshot 2025-12-22 160706" src="https://github.com/user-attachments/assets/68abd078-1a22-4d91-b46b-5171a98c0720" />
<img width="1266" height="495" alt="Screenshot 2025-12-22 160518" src="https://github.com/user-attachments/assets/fb9cf0f5-a270-45ae-8938-46881a4f0070" />
<img width="988" height="508" alt="Screenshot 2025-12-22 160407" src="https://github.com/user-attachments/assets/aa68e7fd-c0d4-4f05-b832-a8da95f8bbca" />
<img width="1325" height="498" alt="Screenshot 2025-12-22 154152" src="https://github.com/user-attachments/assets/76b1c765-59cc-4163-961c-f9f924162950" />
<img width="858" height="663" alt="Screenshot 2025-12-22 153850" src="https://github.com/user-attachments/assets/fc4983af-a681-4788-bdd4-35e55b7c34d0" />
<img width="890" height="433" alt="Screenshot 2025-12-22 153800" src="https://github.com/user-attachments/assets/73a4f58c-2391-4878-b9dc-b81a9820c650" />
<img width="907" height="488" alt="Screenshot 2025-12-22 153202" src="https://github.com/user-attachments/assets/fcf4f2d6-c13e-4e85-8fd8-a5d2a1d50e1b" />
<img width="1327" height="549" alt="Screenshot 2025-12-22 151028" src="https://github.com/user-attachments/assets/225fa07e-f3c2-4dbf-8b39-496de6dfd85e" />
<img width="1138" height="467" alt="Screenshot 2025-12-22 150631" src="https://github.com/user-attachments/assets/fae6edb3-9161-432a-b72f-4da8aad8483a" />
<img width="1055" height="450" alt="Screenshot 2025-12-22 143958" src="https://github.com/user-attachments/assets/55e83748-41bc-49ef-b1ee-95bf78ec76c8" />
<img width="782" height="454" alt="Screenshot 2025-12-22 143557" src="https://github.com/user-attachments/assets/218eae42-7c30-414d-b2ef-2bb3a2a9f424" />
<img width="1090" height="505" alt="Screenshot 2025-12-22 142019" src="https://github.com/user-attachments/assets/835f4f43-1252-4b2c-b262-6d63c0887183" />
<img width="580" height="388" alt="Screenshot 2025-12-22 141215" src="https://github.com/user-attachments/assets/de9425b6-8127-42ec-b21b-157ab88bea6f" />
<img width="877" height="441" alt="Screenshot 2025-12-22 134303" src="https://github.com/user-attachments/assets/07112db4-90d8-4559-bd46-a2911f000eef" />
<img width="1119" height="479" alt="Screenshot 2025-12-22 133359" src="https://github.com/user-attachments/assets/a56bf17e-2164-4310-91c9-ff9080f3e1c0" />
<img width="423" height="344" alt="Screenshot 2025-12-18 151111" src="https://github.com/user-attachments/assets/88a5b3f8-c0d2-452f-b9fe-ab084fa3fba1" />
<img width="1043" height="305" alt="Screenshot 2025-12-18 104300" src="https://github.com/user-attachments/assets/2023ef10-87c8-4445-aa3d-5fbdf2de5c82" />
<img width="1231" height="629" alt="Screenshot 2025-12-17 155342" src="https://github.com/user-attachments/assets/88a4b708-4dae-4ed8-bc59-01e76800df07" />
<img width="616" height="537" alt="Screenshot 2025-12-17 104222" src="https://github.com/user-attachments/assets/811ccf71-2cd0-41e5-b508-e4e251608aef" />
<img width="1331" height="568" alt="Screenshot 2025-12-17 101054" src="https://github.com/user-attachments/assets/d7a81bdd-0867-4269-8d39-66ea542ded7c" />
<img width="1332" height="198" alt="Screenshot 2025-12-16 102950" src="https://github.com/user-attachments/assets/b19e959f-3381-4d4c-8e8e-217369a608b1" />




## Pub/Sub to BigQuery – Implementation Summary

1. Pub/Sub Topic and Subscription
- A Pub/Sub topic named 'sainathbigquery_events' was created.
- A subscription named 'sainathbigquery-events-sub' was created for the topic.
- The subscription is active and able to receive messages.
- Messages published to the topic are successfully delivered to the subscription.
2. Publishing Messages to Pub/Sub
- User event messages are published in JSON format.
- Each message contains event type and user information.
- Example events include user login actions.
- Messages are successfully accepted by Pub/Sub.
3. Cloud Function Deployment
- A Cloud Function named 'sainathfunctionapp' was deployed in the asia-south1 region.
- The function is configured with a Pub/Sub trigger.
- It runs automatically whenever a message is published to the topic.
4. Message Processing in Cloud Function
- The Cloud Function decodes the Pub/Sub message.
- JSON data is extracted from the message payload.
- A timestamp is generated during processing.
- The processed data is prepared for storage in BigQuery.
<img width="900" height="414" alt="image" src="https://github.com/user-attachments/assets/67605832-1a94-4f20-8f12-d3d61cb32679" />

  
5. BigQuery Dataset and Table
- A BigQuery dataset named 'sainathevents' was created.
- A table named 'user_events' was created inside the dataset.
- Table schema includes event, user, and timestamp fields.
 <img width="900" height="387" alt="image" src="https://github.com/user-attachments/assets/d525df85-e849-41c5-8af5-63372edcfa3b" />


6. Data Insertion into BigQuery
- The Cloud Function inserts processed records into the BigQuery table.
- Multiple records are stored successfully.
- Each record contains event name, user name, and timestamp.
 <img width="900" height="405" alt="image" src="https://github.com/user-attachments/assets/d17e5551-be82-48f7-a8f3-bb84bd533400" />


7. End-to-End Data Flow
- Events are published to Pub/Sub.
- Pub/Sub triggers the Cloud Function.
- The Cloud Function processes the data.
- BigQuery stores the final records for analysis.
 <img width="900" height="434" alt="image" src="https://github.com/user-attachments/assets/8ca6255c-443c-445e-8d4e-9bf556649a52" />


Conclusion
This implementation demonstrates a real-time event processing system using Google Cloud Pub/Sub, Cloud Functions, and BigQuery. The solution is scalable, reliable, and suitable for real-time data analytics.
