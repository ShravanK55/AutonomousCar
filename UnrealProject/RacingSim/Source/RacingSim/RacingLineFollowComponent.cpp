// Fill out your copyright notice in the Description page of Project Settings.

#include "RacingLineFollowComponent.h"
#include "Kismet/KismetMathLibrary.h"
#include "WheeledVehicleMovementComponent.h"


// Sets default values for this component's properties
URacingLineFollowComponent::URacingLineFollowComponent()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = true;

	RaceCarRef = Cast<ARacingSimPawn>(GetOwner());
}


// Called when the game starts
void URacingLineFollowComponent::BeginPlay()
{
	Super::BeginPlay();

	RaceCarRef = Cast<ARacingSimPawn>(GetOwner());
}


// Called every frame
void URacingLineFollowComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

	CalculateSteeringAngle();
	CalculateThrottle();
}


void URacingLineFollowComponent::CalculateSteeringAngle()
{
	if (RaceCarRef && RacingLineRef)
	{
		FVector CarLocation = RaceCarRef->GetActorLocation();

		FVector RightVectorToRaceLine = RacingLineRef->FindRightVectorClosestToWorldLocation(CarLocation, ESplineCoordinateSpace::Local);
		FRotator RightVecRotator = UKismetMathLibrary::MakeRotationFromAxes(RightVectorToRaceLine, FVector(0.0f), FVector(0.0f));

		FVector X, Y, Z;
		UKismetMathLibrary::BreakRotIntoAxes(RightVecRotator, X, Y, Z);
		FRotator RotatorToRacingLine = UKismetMathLibrary::MakeRotFromX(Y);
		FVector VectorToRacingLine = UKismetMathLibrary::GetForwardVector(RotatorToRacingLine) * 500;

		FVector RacingLinePoint = CarLocation - VectorToRacingLine;

		FVector LocationClosestToRacingLine = RacingLineRef->FindLocationClosestToWorldLocation(RacingLinePoint, ESplineCoordinateSpace::World);
		RaceCarRef->Steering = LocationClosestToRacingLine;
		SphereLocation = LocationClosestToRacingLine;

		float Roll, Pitch, Yaw;
		UKismetMathLibrary::BreakRotator(RightVecRotator, Roll, Pitch, Yaw);
		Yaw -= 180.0f;

		ArrowLocation = RacingLineRef->FindLocationClosestToWorldLocation(CarLocation, ESplineCoordinateSpace::World);
		ArrowRotation = UKismetMathLibrary::MakeRotator(Roll, Pitch, Yaw);
	}
}


void URacingLineFollowComponent::CalculateThrottle()
{
	if (RaceCarRef && RacingLineRef)
	{
		float VehicleSpeed = RaceCarRef->GetVehicleMovement()->GetForwardSpeed() * 0.036;
		
		if (VehicleSpeed < 20.0f)
		{
			RaceCarRef->Throttle = 1.0f;
		}
		else
		{
			FVector VehicleLocation2D = FVector(RaceCarRef->GetActorLocation().X,
												RaceCarRef->GetActorLocation().Y,
												0.0f);
			FVector ArrowLocation2D = FVector(ArrowLocation.X,
											  ArrowLocation.Y,
											  0.0f);

			float VectorMagnitude = (VehicleLocation2D - ArrowLocation2D).Size();

			if (VehicleSpeed * VectorMagnitude < 1000.0f)
			{
				RaceCarRef->Throttle = 1.0f;
			}
			else
			{
				RaceCarRef->Throttle = UKismetMathLibrary::MapRangeUnclamped(VehicleSpeed * VectorMagnitude,
																			 0, 10000, 1, 0.65);
			}
		}
	}
}
