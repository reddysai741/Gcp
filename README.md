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
