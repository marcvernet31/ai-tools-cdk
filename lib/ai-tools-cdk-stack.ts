import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import * as dotenv from 'dotenv';

dotenv.config();

export class AiToolsCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // TODO: Generate with cdk
    const openaiLayer = lambda.LayerVersion.fromLayerVersionArn(this, 'OpenaiAPI', 'arn:aws:lambda:us-east-1:236272758067:layer:openai:1')
    const pytubeLayer = lambda.LayerVersion.fromLayerVersionArn(this, 'PyTube', 'arn:aws:lambda:us-east-1:236272758067:layer:pytube:1')

    new lambda.Function(this, 'YoutubeTranscriptFunction', {
      functionName: 'YoutubeTranscript',
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset(path.join(__dirname, '/../src/lambda')),
      handler: 'index.handler',
      layers: [openaiLayer, pytubeLayer],
      timeout: cdk.Duration.minutes(1),
      environment: {
        OPENAI_KEY: process.env.OPENAI_KEY || ''
      }
    });
  }
}
