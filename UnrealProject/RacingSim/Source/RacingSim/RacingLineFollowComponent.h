// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "Components/SplineComponent.h"
#include "RacingSimPawn.h"
#include "RacingLineFollowComponent.generated.h"


UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class RACINGSIM_API URacingLineFollowComponent : public UActorComponent
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	URacingLineFollowComponent();

protected:
	// Called when the game starts
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

public:
	/** Reference to the racing line to race on. */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	USplineComponent* RacingLineRef = nullptr;
	
	/** Reference to the race car to control. */
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	ARacingSimPawn* RaceCarRef = nullptr;

	UPROPERTY(VisibleAnywhere, BlueprintReadWrite)
	FVector SphereLocation;

	UPROPERTY(VisibleAnywhere, BlueprintReadWrite)
	FVector ArrowLocation;

	UPROPERTY(VisibleAnywhere, BlueprintReadWrite)
	FRotator ArrowRotation;

	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	float SteeringLookAhead;

public:
	UFUNCTION(BlueprintCallable)
	void CalculateSteeringAngle();

	UFUNCTION(BlueprintCallable)
	void CalculateThrottle();
};
